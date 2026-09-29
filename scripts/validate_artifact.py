#!/usr/bin/env python3
"""Validate route-plan and evidence-bundle JSON without third-party packages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROUTE_REQUIRED = {
    "schema_version", "request_id", "decision", "scope", "selected_skills",
    "execution_order", "missing_inputs", "artifacts", "boundaries"
}
EVIDENCE_REQUIRED = {
    "schema_version", "bundle_id", "product", "scope", "evidence", "assumptions", "blockers"
}
KINDS = {"observed", "calculated", "modeled", "inferred", "assumed"}


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def require_list(value: Any, label: str, nonempty: bool = False) -> list[Any]:
    if not isinstance(value, list) or (nonempty and not value):
        suffix = " and non-empty" if nonempty else ""
        raise ValueError(f"{label} must be a list{suffix}")
    return value


def validate_route(data: dict[str, Any]) -> None:
    missing = ROUTE_REQUIRED - set(data)
    if missing:
        raise ValueError(f"missing route field(s): {', '.join(sorted(missing))}")
    if data["schema_version"] != "1.0":
        raise ValueError("unsupported route schema_version")
    scope = require_object(data["scope"], "scope")
    for key in ("marketplace", "as_of"):
        if not scope.get(key):
            raise ValueError(f"scope.{key} is required")
    selected = require_list(data["selected_skills"], "selected_skills", nonempty=True)
    names = set()
    for index, item in enumerate(selected):
        item = require_object(item, f"selected_skills[{index}]")
        for key in ("skill_name", "reason", "status"):
            if not item.get(key):
                raise ValueError(f"selected_skills[{index}].{key} is required")
        names.add(item["skill_name"])
    order = require_list(data["execution_order"], "execution_order", nonempty=True)
    unknown = [name for name in order if name not in names]
    if unknown:
        raise ValueError(f"execution_order contains unselected skill(s): {', '.join(unknown)}")
    for key in ("missing_inputs", "artifacts", "boundaries"):
        require_list(data[key], key)


def validate_evidence(data: dict[str, Any]) -> None:
    missing = EVIDENCE_REQUIRED - set(data)
    if missing:
        raise ValueError(f"missing evidence field(s): {', '.join(sorted(missing))}")
    if data["schema_version"] != "1.0":
        raise ValueError("unsupported evidence schema_version")
    require_object(data["product"], "product")
    require_object(data["scope"], "scope")
    evidence = require_list(data["evidence"], "evidence")
    ids = set()
    for index, item in enumerate(evidence):
        item = require_object(item, f"evidence[{index}]")
        for key in ("evidence_id", "claim", "kind", "source", "confidence"):
            if key not in item:
                raise ValueError(f"evidence[{index}].{key} is required")
        if item["evidence_id"] in ids:
            raise ValueError(f"duplicate evidence_id: {item['evidence_id']}")
        ids.add(item["evidence_id"])
        if item["kind"] not in KINDS:
            raise ValueError(f"invalid evidence kind: {item['kind']}")
        confidence = item["confidence"]
        if isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            raise ValueError(f"evidence[{index}].confidence must be between 0 and 1")
        source = require_object(item["source"], f"evidence[{index}].source")
        for key in ("type", "locator", "accessed_at"):
            if not source.get(key):
                raise ValueError(f"evidence[{index}].source.{key} is required")
    require_list(data["assumptions"], "assumptions")
    require_list(data["blockers"], "blockers")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("route-plan", "evidence-bundle"))
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
        data = require_object(data, "document root")
        if args.kind == "route-plan":
            validate_route(data)
        else:
            validate_evidence(data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"invalid: {exc}", file=sys.stderr)
        return 2
    print(f"valid {args.kind}: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
