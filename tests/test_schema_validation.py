"""Tests for JSON Schema validation of reference catalogs."""

import json
import tempfile
import unittest
from pathlib import Path

from tools.validator import validate_catalog_json

REPO_ROOT = Path(__file__).resolve().parents[1]


class TestSchemaValidation(unittest.TestCase):
    def _catalog(self, name: str, data) -> tuple[Path, Path]:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        (root / "schemas").mkdir()
        schema_src = REPO_ROOT / "schemas" / "authoritative-domains.schema.json"
        (root / "schemas" / "authoritative-domains.schema.json").write_text(
            schema_src.read_text(encoding="utf-8"), encoding="utf-8"
        )
        path = root / name
        path.write_text(json.dumps(data), encoding="utf-8")
        return path, root

    def test_all_schemas_declare_draft_07(self):
        for schema_path in (REPO_ROOT / "schemas").glob("*.json"):
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            self.assertEqual(
                schema.get("$schema"), "http://json-schema.org/draft-07/schema#", schema_path.name
            )
            self.assertNotIn("", schema, f"{schema_path.name} has an empty-string key")

    def test_valid_catalog_passes(self):
        path, root = self._catalog(
            "authoritative-domains.json",
            {"version": 1, "domains": [{"domain": "example.com", "category": "demo"}]},
        )
        self.assertEqual(validate_catalog_json(path, root), [])

    def test_missing_required_field_fails(self):
        path, root = self._catalog("authoritative-domains.json", {"version": 1})
        errors = validate_catalog_json(path, root)
        self.assertEqual(len(errors), 1)
        self.assertIn("Schema validation failed", errors[0])

    def test_wrong_type_fails(self):
        path, root = self._catalog(
            "authoritative-domains.json", {"version": "one", "domains": []}
        )
        self.assertIn("Schema validation failed", validate_catalog_json(path, root)[0])

    def test_non_object_root_fails(self):
        path, root = self._catalog("authoritative-domains.json", "just a string")
        self.assertIn("JSON root must be an object or array", validate_catalog_json(path, root)[0])


if __name__ == "__main__":
    unittest.main()
