from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class UnitEconomicsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module(
            "unit_economics",
            ROOT / "skills" / "amazon-unit-economics-cashflow" / "scripts" / "unit_economics.py",
        )

    def test_example_reconciles_and_contains_downside_scenarios(self) -> None:
        result = self.module.calculate(self.module.EXAMPLE)
        self.assertEqual(result["schema_version"], "1.0")
        self.assertEqual(len(result["scenarios"]), 2)
        base = result["base"]["per_unit"]
        self.assertAlmostEqual(base["contribution_profit"], 6.68341, places=4)
        self.assertAlmostEqual(base["contribution_margin"], 0.222854, places=5)
        self.assertGreater(base["break_even_acos"], self.module.EXAMPLE["advertising_acos"])
        self.assertTrue(all(case["per_unit"]["contribution_profit"] < base["contribution_profit"] for case in result["scenarios"]))

    def test_invalid_rate_is_rejected(self) -> None:
        data = dict(self.module.EXAMPLE)
        data["return_rate"] = 1.1
        with self.assertRaisesRegex(ValueError, "between 0 and 1"):
            self.module.calculate(data)

    def test_first_order_cash_is_separate_from_per_unit_profit(self) -> None:
        result = self.module.calculate(self.module.EXAMPLE)["base"]
        cash = result["first_order_cash"]
        self.assertEqual(cash["purchase_order_total"], 7800.0)
        self.assertEqual(cash["total_first_order_cash_required"], 12550.0)


class ArtifactValidationTests(unittest.TestCase):
    def run_validator(self, kind: str, path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [PYTHON, str(ROOT / "scripts" / "validate_artifact.py"), kind, str(path)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_example_artifacts_are_valid(self) -> None:
        example = ROOT / "examples" / "magnetic-car-phone-mount"
        self.assertEqual(self.run_validator("route-plan", example / "route-plan.json").returncode, 0)
        self.assertEqual(self.run_validator("evidence-bundle", example / "evidence-bundle.json").returncode, 0)

    def test_duplicate_evidence_id_is_rejected(self) -> None:
        source = ROOT / "examples" / "magnetic-car-phone-mount" / "evidence-bundle.json"
        data = json.loads(source.read_text(encoding="utf-8"))
        data["evidence"].append(dict(data["evidence"][0]))
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "invalid.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_validator("evidence-bundle", path)
        self.assertEqual(result.returncode, 2)
        self.assertIn("duplicate evidence_id", result.stderr)


class CatalogAndInstallerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.installer = load_module("install_suite", ROOT / "scripts" / "install_suite.py")

    def test_trigger_matrix_covers_positive_and_negative_cases(self) -> None:
        cases = json.loads((ROOT / "tests" / "trigger-cases.json").read_text(encoding="utf-8"))
        expected = {
            "amazon-product-research-suite",
            "amazon-product-differentiation-rd",
            "amazon-supplier-feasibility",
            "amazon-unit-economics-cashflow",
        }
        self.assertEqual(set(cases), expected)
        for skill_name, matrix in cases.items():
            self.assertGreaterEqual(len(matrix["should_trigger"]), 2, skill_name)
            self.assertGreaterEqual(len(matrix["should_not_trigger"]), 2, skill_name)

    def test_catalog_validator(self) -> None:
        result = subprocess.run(
            [PYTHON, str(ROOT / "scripts" / "validate_catalog.py")],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("7 skills", result.stdout)

    def test_installer_dry_run_does_not_create_target(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "not-created"
            result = subprocess.run(
                [PYTHON, str(ROOT / "scripts" / "install_suite.py"), "--dry-run", "--target", str(target)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(target.exists())
            self.assertIn("no files were written", result.stdout)

    def test_installer_stages_nested_skill_and_preserves_existing_destination(self) -> None:
        skill = {
            "id": "fixture-skill",
            "repository": "owner/repository",
            "ref": "v1.0.0",
            "path": "skills/fixture-skill",
            "skill_name": "fixture-skill",
        }
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr("repository-v1.0.0/skills/fixture-skill/SKILL.md", "---\nname: fixture-skill\ndescription: Fixture.\n---\n")
        cache = {(skill["repository"], skill["ref"]): buffer.getvalue()}
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "skills"
            self.assertTrue(self.installer.install_one(skill, target, False, False, cache))
            destination = target / "fixture-skill"
            marker = json.loads((destination / ".suite-install.json").read_text(encoding="utf-8"))
            self.assertEqual(marker["ref"], "v1.0.0")
            (destination / "local-change.txt").write_text("preserve", encoding="utf-8")
            self.assertFalse(self.installer.install_one(skill, target, False, False, cache))
            self.assertEqual((destination / "local-change.txt").read_text(encoding="utf-8"), "preserve")


if __name__ == "__main__":
    unittest.main()
