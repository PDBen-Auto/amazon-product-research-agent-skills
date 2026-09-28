#!/usr/bin/env python3
"""Validate the suite catalog without network access."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "skills.json"
REQUIRED = {"id", "name", "repository", "skill_name", "url", "install", "triggers", "outputs"}


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    assert data.get("schema_version") == "1.0"
    skills = data.get("skills")
    assert isinstance(skills, list) and skills, "catalog must contain skills"
    ids = set()
    for skill in skills:
        assert REQUIRED <= set(skill), f"missing fields for {skill.get('id')}"
        assert skill["id"] not in ids, f"duplicate id: {skill['id']}"
        assert skill["repository"].count("/") == 1
        assert skill["url"].startswith("https://github.com/")
        assert skill["triggers"] and skill["outputs"]
        ids.add(skill["id"])
    print(f"catalog valid: {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
