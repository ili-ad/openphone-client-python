from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from scripts.spec_table import OUTPUT_PATH, SPEC_PATH, generate_endpoints_markdown


def _normalize_newlines(content: str) -> str:
    normalized = content.replace("\r\n", "\n")
    if not normalized.endswith("\n"):
        normalized += "\n"
    return normalized


def main() -> int:
    expected = _normalize_newlines(generate_endpoints_markdown(SPEC_PATH))
    current = _normalize_newlines(OUTPUT_PATH.read_text())

    if expected != current:
        print(
            "spec/endpoints.md is out of date. Run: poetry run python scripts/spec_table.py and commit the result."
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
