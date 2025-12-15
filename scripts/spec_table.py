from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterator, Tuple

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "spec" / "quo-openapi-v1.json"
OUTPUT_PATH = ROOT / "spec" / "endpoints.md"

METHOD_ORDER = [
    "delete",
    "get",
    "head",
    "options",
    "patch",
    "post",
    "put",
]


def _iter_operations(paths: Dict[str, Dict[str, dict]]) -> Iterator[Tuple[str, str, dict]]:
    for path in sorted(paths):
        path_item = paths[path] or {}
        for method in METHOD_ORDER:
            operation = path_item.get(method)
            if operation:
                yield method.upper(), path, operation

        remaining = sorted(
            method
            for method in path_item
            if not method.startswith("x-") and method not in METHOD_ORDER
        )
        for method in remaining:
            operation = path_item[method]
            if operation:
                yield method.upper(), path, operation


def _escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def build_table(spec: dict) -> str:
    header = [
        "# Endpoint inventory",
        "",
        "Generated from spec/quo-openapi-v1.json. Do not edit by hand.",
        "",
        "| Method | Path | Operation ID | Summary |",
        "| --- | --- | --- | --- |",
    ]

    rows = []
    paths = spec.get("paths", {})
    for method, path, operation in _iter_operations(paths):
        rows.append(
            "| {method} | {path} | {operation_id} | {summary} |".format(
                method=method,
                path=path,
                operation_id=_escape(operation.get("operationId", "")),
                summary=_escape(operation.get("summary", "")),
            )
        )

    return "\n".join([*header, *rows]) + "\n"


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text())
    content = build_table(spec)
    OUTPUT_PATH.write_text(content)
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
