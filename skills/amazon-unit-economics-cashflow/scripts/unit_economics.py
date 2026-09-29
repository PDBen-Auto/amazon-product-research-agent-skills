#!/usr/bin/env python3
"""Calculate Amazon product unit economics from explicit JSON assumptions."""

from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any


EXAMPLE: dict[str, Any] = {
    "scenario_name": "illustrative-base",
    "marketplace": "Amazon US",
    "currency": "USD",
    "selling_price": 29.99,
    "referral_fee_rate": 0.15,
    "fulfillment_fee": 4.25,
    "landed_product_cost": 7.8,
    "return_rate": 0.06,
    "return_loss_per_return": 8.0,
    "advertising_acos": 0.14,
    "other_variable_cost": 0.55,
    "order_units": 1000,
    "tooling_cost": 1800.0,
    "setup_cost": 450.0,
    "deposit_rate": 0.3,
    "working_capital_buffer": 2500.0,
    "scenarios": [
        {"name": "higher-returns", "overrides": {"return_rate": 0.14}},
        {"name": "higher-ad-spend", "overrides": {"advertising_acos": 0.25}}
    ]
}

REQUIRED_NUMBERS = {
    "selling_price",
    "referral_fee_rate",
    "fulfillment_fee",
    "landed_product_cost",
    "return_rate",
    "return_loss_per_return",
    "advertising_acos",
    "other_variable_cost",
}
OPTIONAL_NUMBERS = {
    "order_units": 0,
    "tooling_cost": 0.0,
    "setup_cost": 0.0,
    "deposit_rate": 0.0,
    "working_capital_buffer": 0.0,
}
RATES = {"referral_fee_rate", "return_rate", "advertising_acos", "deposit_rate"}


def _number(data: dict[str, Any], key: str) -> float:
    value = data[key]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{key} must be a number")
    value = float(value)
    if value < 0:
        raise ValueError(f"{key} must be non-negative")
    if key in RATES and value > 1:
        raise ValueError(f"{key} must be between 0 and 1")
    return value


def validate(data: dict[str, Any]) -> dict[str, Any]:
    missing = sorted(REQUIRED_NUMBERS - set(data))
    if missing:
        raise ValueError(f"missing required field(s): {', '.join(missing)}")
    normalized = deepcopy(data)
    for key, default in OPTIONAL_NUMBERS.items():
        normalized.setdefault(key, default)
    for key in REQUIRED_NUMBERS | set(OPTIONAL_NUMBERS):
        normalized[key] = _number(normalized, key)
    if normalized["selling_price"] <= 0:
        raise ValueError("selling_price must be greater than zero")
    if normalized["order_units"] != int(normalized["order_units"]):
        raise ValueError("order_units must be a whole number")
    normalized["order_units"] = int(normalized["order_units"])
    for key in ("scenario_name", "marketplace", "currency"):
        normalized.setdefault(key, "unspecified")
        if not isinstance(normalized[key], str) or not normalized[key].strip():
            raise ValueError(f"{key} must be a non-empty string")
    return normalized


def calculate_case(data: dict[str, Any]) -> dict[str, Any]:
    values = validate(data)
    price = values["selling_price"]
    realized_revenue = price * (1 - values["return_rate"])
    referral_fee = realized_revenue * values["referral_fee_rate"]
    advertising_cost = price * values["advertising_acos"]
    expected_return_loss = values["return_rate"] * values["return_loss_per_return"]
    non_ad_cost = (
        referral_fee
        + values["fulfillment_fee"]
        + values["landed_product_cost"]
        + expected_return_loss
        + values["other_variable_cost"]
    )
    contribution_profit = realized_revenue - non_ad_cost - advertising_cost
    break_even_acos = max(0.0, (realized_revenue - non_ad_cost) / price)
    purchase_order_total = values["order_units"] * values["landed_product_cost"]
    result = {
        "scenario_name": values["scenario_name"],
        "marketplace": values["marketplace"],
        "currency": values["currency"],
        "per_unit": {
            "selling_price": price,
            "realized_revenue_after_returns": realized_revenue,
            "referral_fee": referral_fee,
            "fulfillment_fee": values["fulfillment_fee"],
            "landed_product_cost": values["landed_product_cost"],
            "expected_return_loss": expected_return_loss,
            "advertising_cost": advertising_cost,
            "other_variable_cost": values["other_variable_cost"],
            "contribution_profit": contribution_profit,
            "contribution_margin": contribution_profit / price,
            "break_even_acos": break_even_acos,
        },
        "first_order_cash": {
            "order_units": values["order_units"],
            "purchase_order_total": purchase_order_total,
            "cash_due_at_order": purchase_order_total * values["deposit_rate"],
            "cash_due_before_shipment": purchase_order_total * (1 - values["deposit_rate"]),
            "tooling_cost": values["tooling_cost"],
            "setup_cost": values["setup_cost"],
            "working_capital_buffer": values["working_capital_buffer"],
            "total_first_order_cash_required": purchase_order_total
            + values["tooling_cost"]
            + values["setup_cost"]
            + values["working_capital_buffer"],
        },
    }
    return _round_numbers(result)


def _round_numbers(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 6)
    if isinstance(value, dict):
        return {key: _round_numbers(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_round_numbers(item) for item in value]
    return value


def calculate(data: dict[str, Any]) -> dict[str, Any]:
    base_input = deepcopy(data)
    scenarios = base_input.pop("scenarios", [])
    if not isinstance(scenarios, list):
        raise ValueError("scenarios must be a list")
    result = {"schema_version": "1.0", "base": calculate_case(base_input), "scenarios": []}
    for scenario in scenarios:
        if not isinstance(scenario, dict) or not isinstance(scenario.get("overrides"), dict):
            raise ValueError("each scenario must contain an overrides object")
        case = deepcopy(base_input)
        case.update(scenario["overrides"])
        case["scenario_name"] = str(scenario.get("name", "unnamed-scenario"))
        result["scenarios"].append(calculate_case(case))
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="JSON assumptions file")
    parser.add_argument("--output", type=Path, help="write JSON to this path instead of stdout")
    parser.add_argument("--pretty", action="store_true", help="indent output JSON")
    parser.add_argument("--example", action="store_true", help="print an illustrative input document")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.example:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    if args.input is None:
        print("input JSON path is required unless --example is used", file=sys.stderr)
        return 2
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("input root must be an object")
        result = calculate(data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
