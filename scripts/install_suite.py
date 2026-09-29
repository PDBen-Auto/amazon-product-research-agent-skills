#!/usr/bin/env python3
"""Install pinned public child Skills into a local Agent Skills directory."""

from __future__ import annotations

import argparse
import io
import json
import shutil
import sys
import tempfile
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "skills.json"
MARKER = ".suite-install.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=Path.home() / ".codex" / "skills")
    parser.add_argument("--skill", action="append", dest="skills", help="catalog id; repeatable")
    parser.add_argument("--dry-run", action="store_true", help="show the pinned installation plan without writing")
    parser.add_argument("--list", action="store_true", help="list catalog Skills and exit")
    parser.add_argument("--check", action="store_true", help="check installed versions without network access")
    parser.add_argument("--force", action="store_true", help="replace an existing destination after staging succeeds")
    return parser.parse_args()


def load_catalog() -> list[dict[str, Any]]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    return list(data["skills"])


def select_skills(catalog: list[dict[str, Any]], requested: list[str] | None) -> list[dict[str, Any]]:
    known = {str(item["id"]) for item in catalog}
    unknown = set(requested or []) - known
    if unknown:
        raise ValueError(f"unknown catalog id(s): {', '.join(sorted(unknown))}")
    return catalog if not requested else [item for item in catalog if item["id"] in set(requested)]


def archive_url(repo: str, ref: str) -> str:
    owner, name = repo.split("/", 1)
    return f"https://codeload.github.com/{owner}/{name}/zip/{urllib.parse.quote(ref, safe='')}"


def download_archive(repo: str, ref: str) -> bytes:
    request = urllib.request.Request(
        archive_url(repo, ref),
        headers={"User-Agent": "amazon-product-research-agent-skills-installer"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def safe_member_path(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts:
        raise RuntimeError(f"unsafe archive member: {name}")
    return path


def extract_archive(archive: bytes, destination: Path) -> Path:
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        names = [name for name in zipped.namelist() if name and not name.endswith("/")]
        if not names:
            raise RuntimeError("downloaded archive is empty")
        roots = {safe_member_path(name).parts[0] for name in names}
        if len(roots) != 1:
            raise RuntimeError("archive must contain exactly one root directory")
        root_name = next(iter(roots))
        for name in zipped.namelist():
            path = safe_member_path(name)
            relative_parts = path.parts[1:]
            if not relative_parts:
                continue
            output = destination.joinpath(*relative_parts)
            if name.endswith("/"):
                output.mkdir(parents=True, exist_ok=True)
                continue
            output.parent.mkdir(parents=True, exist_ok=True)
            with zipped.open(name) as source, output.open("wb") as target:
                shutil.copyfileobj(source, target)
    if not root_name:
        raise RuntimeError("archive root not found")
    return destination


def source_root(extracted: Path, skill: dict[str, Any]) -> Path:
    configured = PurePosixPath(str(skill.get("path", ".")))
    candidate = extracted.joinpath(*configured.parts) if str(configured) != "." else extracted
    if (candidate / "SKILL.md").is_file():
        return candidate
    matches = [path.parent for path in extracted.rglob("SKILL.md") if path.parent.name == skill["skill_name"]]
    if len(matches) == 1:
        return matches[0]
    raise RuntimeError(f"SKILL.md for {skill['skill_name']} not found at {configured}")


def marker_payload(skill: dict[str, Any]) -> dict[str, Any]:
    return {
        "installer": "amazon-product-research-agent-skills",
        "catalog_id": skill["id"],
        "repository": skill["repository"],
        "ref": skill["ref"],
        "skill_name": skill["skill_name"],
        "installed_at": datetime.now(timezone.utc).isoformat(),
    }


def install_one(
    skill: dict[str, Any],
    target: Path,
    dry_run: bool,
    force: bool,
    cache: dict[tuple[str, str], bytes],
) -> bool:
    destination = target / str(skill["skill_name"])
    label = f"{skill['repository']}@{skill['ref']}:{skill.get('path', '.')} -> {destination}"
    print(f"- {label}")
    if dry_run:
        return True
    if destination.exists() and not force:
        print(f"  skipped: destination exists; use --check or explicit --force", file=sys.stderr)
        return False
    key = (str(skill["repository"]), str(skill["ref"]))
    if key not in cache:
        cache[key] = download_archive(*key)
    archive = cache[key]
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"suite-{skill['skill_name']}-", dir=target) as temp_name:
        temp = Path(temp_name)
        extracted = extract_archive(archive, temp / "archive")
        source = source_root(extracted, skill)
        staged = temp / "staged"
        shutil.copytree(source, staged)
        (staged / MARKER).write_text(
            json.dumps(marker_payload(skill), indent=2) + "\n", encoding="utf-8"
        )
        if not (staged / "SKILL.md").is_file():
            raise RuntimeError("staged Skill is missing SKILL.md")
        backup = temp / "previous"
        if destination.exists():
            destination.rename(backup)
        try:
            staged.rename(destination)
        except Exception:
            if backup.exists() and not destination.exists():
                backup.rename(destination)
            raise
    return True


def check_one(skill: dict[str, Any], target: Path) -> bool:
    destination = target / str(skill["skill_name"])
    marker_path = destination / MARKER
    if not (destination / "SKILL.md").is_file():
        print(f"MISSING  {skill['skill_name']}  expected {destination}")
        return False
    if not marker_path.is_file():
        print(f"UNTRACKED {skill['skill_name']}  installed without {MARKER}")
        return False
    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print(f"INVALID  {skill['skill_name']}  unreadable {MARKER}")
        return False
    if marker.get("ref") != skill["ref"] or marker.get("repository") != skill["repository"]:
        print(f"OUTDATED {skill['skill_name']}  installed {marker.get('ref')} expected {skill['ref']}")
        return False
    print(f"CURRENT  {skill['skill_name']}  {skill['ref']}")
    return True


def main() -> int:
    args = parse_args()
    try:
        catalog = load_catalog()
        selected = select_skills(catalog, args.skills)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.list:
        for item in selected:
            print(f"{item['id']:<38} {item['skill_name']:<42} {item['ref']}")
        return 0
    print(f"Target: {args.target.resolve()}")
    if args.check:
        checks = [check_one(item, args.target) for item in selected]
        return 0 if all(checks) else 3
    cache: dict[tuple[str, str], bytes] = {}
    try:
        results = [install_one(item, args.target, args.dry_run, args.force, cache) for item in selected]
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.dry_run:
        print("Dry run complete; no files were written.")
        return 0
    if not all(results):
        print("Install incomplete because existing destinations were preserved.", file=sys.stderr)
        return 3
    print("Install complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
