"""Unit tests verifying industry references structure and JSON catalogs."""

import json
import unittest
from pathlib import Path


class TestIndustryReferences(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]
        self.ref_dir = self.root / "references"

    def test_references_directory_exists(self):
        self.assertTrue(self.ref_dir.exists())

    def test_all_json_catalogs_are_valid(self):
        catalogs = list(self.ref_dir.rglob("*.json"))
        for cat in catalogs:
            try:
                data = json.loads(cat.read_text(encoding="utf-8"))
                self.assertIsInstance(data, (dict, list))
            except Exception as exc:
                self.fail(f"Catalog {cat.name} failed JSON parsing: {exc}")


if __name__ == "__main__":
    unittest.main()
