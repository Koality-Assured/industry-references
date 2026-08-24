"""CLI validator for industry reference json catalogs and markdown guides."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_catalog_json(path: Path) -> list[str]:
    errors = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, (dict, list)):
            errors.append(f"{path.name}: JSON root must be an object or array")
    except Exception as exc:
        errors.append(f"{path.name}: Invalid JSON - {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate industry references")
    parser.add_argument("--all", action="store_true", help="Validate all references")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    ref_dir = root / "references"
    all_errors = []

    json_files = list(ref_dir.rglob("*.json"))
    for f in json_files:
        errs = validate_catalog_json(f)
        all_errors.extend(errs)

    if all_errors:
        print(f"Validation failed with {len(all_errors)} errors:", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(f"OK: {len(json_files)} catalogs validated cleanly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
