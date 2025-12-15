from __future__ import annotations

import datetime

from openphone_client.api.calls.list_calls_v_1 import sync
from openphone_client.models.list_calls_v1_response_200 import ListCallsV1Response200
from openphone_client.types import UNSET, Unset
from openphone_sdk.request import client


def list_calls(
    phone_number_id: str,
    participants: list[str],
    *,
    user_id: Unset | str = UNSET,
    since: Unset | datetime.datetime = UNSET,
    created_after: Unset | datetime.datetime = UNSET,
    created_before: Unset | datetime.datetime = UNSET,
    max_results: int = 10,
    page_token: Unset | str = UNSET,
) -> ListCallsV1Response200:
    """Return list of calls or raise RuntimeError on non-200."""

    if not participants:
        raise ValueError("participants must include at least one phone number")
    if max_results < 1 or max_results > 100:
        raise ValueError("max_results must be between 1 and 100")

    res = sync(
        client=client(),
        phone_number_id=phone_number_id,
        user_id=user_id,
        participants=participants,
        since=since,
        created_after=created_after,
        created_before=created_before,
        max_results=max_results,
        page_token=page_token,
    )
    if isinstance(res, ListCallsV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
