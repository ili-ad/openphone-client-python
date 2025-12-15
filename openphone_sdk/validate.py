from __future__ import annotations

from openphone_client.types import UNSET


def validate_created_range(created_after: object, created_before: object) -> None:
    """Validate that created_after and created_before form a sensible range."""

    if created_after is UNSET or created_before is UNSET:
        return

    try:
        if created_after > created_before:
            raise ValueError("created_after must be <= created_before")
    except TypeError:
        raise ValueError(
            "created_after and created_before must be comparable datetimes (both naive or both timezone-aware)"
        )
