#!/usr/bin/env python3
"""Validate the suite catalog and bundled Skill paths without network access."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "skills.json"
REQUIRED = {
    "id", "name", "repository", "ref", "path", "skill_name", "url",
    "install", "triggers", "outputs"
}


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    assert data.get("schema_version") == "1.1"
    assert isinstance(data.get("release"), str) and data["release"].startswith("v")
    skills = data.get("skills")
    assert isinstance(skills, list) and skills, "catalog must contain skills"
    ids: set[str] = set()
    skill_names: set[str] = set()
    for skill in skills:
        assert REQUIRED <= set(skill), f"missing fields for {skill.get('id')}"
        assert skill["id"] not in ids, f"duplicate id: {skill['id']}"
        assert skill["skill_name"] not in skill_names, f"duplicate skill_name: {skill['skill_name']}"
        assert skill["repository"].count("/") == 1
        assert skill["ref"] and not any(char.isspace() for char in skill["ref"])
        assert skill["url"].startswith("https://github.com/")
        assert f"--skill {skill['skill_name']}" in skill["install"]
        assert skill["triggers"] and skill["outputs"]
        if skill["repository"] == "PDBen-Auto/amazon-product-research-agent-skills":
            local_path = ROOT.joinpath(*PurePosixPath(skill["path"]).parts)
            assert (local_path / "SKILL.md").is_file(), f"missing bundled Skill: {local_path}"
        ids.add(skill["id"])
        skill_names.add(skill["skill_name"])
    print(f"catalog valid: {len(skills)} skills ({sum(1 for s in skills if s['repository'].endswith('agent-skills'))} bundled)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
