from __future__ import annotations

import datetime

from quo_client.types import UNSET, Unset


def validate_created_range(
    created_after: Unset | datetime.datetime, created_before: Unset | datetime.datetime
) -> None:
    """Validate that created_after/created_before are comparable and ordered."""

    if created_after is UNSET or created_before is UNSET:
        return

    try:
        if created_after > created_before:
            raise ValueError("created_after must be <= created_before")
    except TypeError as exc:  # naive vs aware datetime comparison
        raise ValueError(
            "created_after and created_before must be comparable datetimes (both naive or both timezone-aware)"
        ) from exc
