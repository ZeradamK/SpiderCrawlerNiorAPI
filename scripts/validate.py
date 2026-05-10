#!/usr/bin/env python3
"""Validate agent output against JSON schemas.

Used by deploy-managed-agent.sh to validate subagent outputs before
passing them to the orchestrator.

Usage:
    python3 scripts/validate.py output.json schema.json
"""

import json
import sys
from pathlib import Path


def validate_type(value: object, schema: dict) -> list[str]:
    """Simple JSON schema type validator (subset of JSON Schema Draft 2020-12)."""
    errors: list[str] = []
    expected_type = schema.get("type")

    if expected_type:
        type_map = {
            "string": str,
            "integer": int,
            "number": (int, float),
            "boolean": bool,
            "array": list,
            "object": dict,
            "null": type(None),
        }

        if isinstance(expected_type, list):
            valid_types = tuple(
                t for et in expected_type for t in (
                    (type_map[et],) if not isinstance(type_map[et], tuple) else type_map[et]
                )
            )
        else:
            valid = type_map.get(expected_type)
            valid_types = valid if isinstance(valid, tuple) else (valid,)

        if not isinstance(value, valid_types):
            errors.append(f"Expected type {expected_type}, got {type(value).__name__}")
            return errors

    if isinstance(value, dict) and "properties" in schema:
        for prop, prop_schema in schema["properties"].items():
            if prop in value:
                sub_errors = validate_type(value[prop], prop_schema)
                errors.extend(f"{prop}.{e}" for e in sub_errors)

        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"Missing required property: {req}")

    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            sub_errors = validate_type(item, schema["items"])
            errors.extend(f"[{i}].{e}" for e in sub_errors)

    if isinstance(value, (int, float)):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"Value {value} below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"Value {value} above maximum {schema['maximum']}")

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"String length {len(value)} below minLength {schema['minLength']}")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"String length {len(value)} above maxLength {schema['maxLength']}")
        if "enum" in schema and value not in schema["enum"]:
            errors.append(f"Value '{value}' not in enum {schema['enum']}")

    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: validate.py <output.json> <schema.json>", file=sys.stderr)
        return 2

    output_path = Path(sys.argv[1])
    schema_path = Path(sys.argv[2])

    if not output_path.exists():
        print(f"ERROR: Output file not found: {output_path}", file=sys.stderr)
        return 1

    if not schema_path.exists():
        print(f"ERROR: Schema file not found: {schema_path}", file=sys.stderr)
        return 1

    try:
        output = json.loads(output_path.read_text())
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in output: {e}", file=sys.stderr)
        return 1

    try:
        schema = json.loads(schema_path.read_text())
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in schema: {e}", file=sys.stderr)
        return 1

    errors = validate_type(output, schema)
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} error(s)")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print("VALIDATION PASSED")
        return 0


if __name__ == "__main__":
    sys.exit(main())
