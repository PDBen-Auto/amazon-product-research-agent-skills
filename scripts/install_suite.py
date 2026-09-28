#!/usr/bin/env python3
"""Install the public child skills into a local Agent Skills directory.

This is an explicit, no-telemetry installer. It downloads public GitHub
archives only after the user runs the command and prints every destination.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "skills.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    default_target = Path.home() / ".codex" / "skills"
    parser.add_argument("--target", type=Path, default=default_target)
    parser.add_argument("--skill", action="append", dest="skills", help="catalog id; repeatable")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_catalog() -> list[dict[str, object]]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    return list(data["skills"])


def download_archive(repo: str) -> bytes:
    url = f"https://codeload.github.com/{repo}/zip/refs/heads/main"
    request = urllib.request.Request(url, headers={"User-Agent": "amazon-product-research-agent-skills-installer"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def install_one(skill: dict[str, object], target: Path, dry_run: bool) -> None:
    repo = str(skill["repository"])
    skill_name = str(skill["skill_name"])
    destination = target / skill_name
    print(f"- {repo} -> {destination}")
    if dry_run:
        return
    archive = download_archive(repo)
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        prefix = f"{repo.split('/', 1)[1]}-main/"
        candidates = [name for name in zipped.namelist() if name.startswith(prefix)]
        if not candidates:
            raise RuntimeError(f"archive prefix not found for {repo}")
        temp = target / f".install-{skill_name}"
        if temp.exists():
            shutil.rmtree(temp)
        temp.mkdir(parents=True, exist_ok=True)
        for name in candidates:
            relative = Path(name[len(prefix) :])
            if not relative.parts:
                continue
            output = temp / relative
            if name.endswith("/"):
                output.mkdir(parents=True, exist_ok=True)
                continue
            output.parent.mkdir(parents=True, exist_ok=True)
            with zipped.open(name) as source, output.open("wb") as destination_file:
                shutil.copyfileobj(source, destination_file)
        if not (temp / "SKILL.md").exists():
            nested = next((path for path in temp.rglob("SKILL.md") if path.parent.name == skill_name), None)
            if nested:
                source_root = nested.parent
            else:
                raise RuntimeError(f"SKILL.md not found in {repo}")
        else:
            source_root = temp
        if destination.exists():
            backup = destination.with_name(destination.name + ".backup")
            if backup.exists():
                shutil.rmtree(backup)
            destination.rename(backup)
        shutil.copytree(source_root, destination)
        shutil.rmtree(temp)


def main() -> int:
    args = parse_args()
    catalog = load_catalog()
    selected = catalog if not args.skills else [item for item in catalog if item["id"] in set(args.skills)]
    known = {str(item["id"]) for item in catalog}
    unknown = set(args.skills or []) - known
    if unknown:
        print(f"Unknown catalog id(s): {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2
    args.target.mkdir(parents=True, exist_ok=True)
    print(f"Target: {args.target.resolve()}")
    for skill in selected:
        install_one(skill, args.target, args.dry_run)
    print("Dry run complete." if args.dry_run else "Install complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
