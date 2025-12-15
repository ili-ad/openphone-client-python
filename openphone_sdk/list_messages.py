from __future__ import annotations

from datetime import datetime
from typing import Union

from openphone_sdk.request import client
from openphone_sdk.validate import validate_created_range
from openphone_client.api.messages.list_messages_v_1 import sync
from openphone_client.models.list_messages_v1_response_200 import ListMessagesV1Response200
from openphone_client.types import UNSET, Unset


def list_messages(
    phone_number_id: str,
    participants: list[str],
    *,
    user_id: Union[Unset, str] = UNSET,
    since: Union[Unset, datetime] = UNSET,
    created_after: Union[Unset, datetime] = UNSET,
    created_before: Union[Unset, datetime] = UNSET,
    max_results: int = 10,
    page_token: Union[Unset, str] = UNSET,
) -> ListMessagesV1Response200:
    """Return messages matching filters or raise RuntimeError on non-200."""

    if not participants:
        raise ValueError("participants must include at least one phone number")
    if max_results < 1 or max_results > 100:
        raise ValueError("max_results must be between 1 and 100")
    validate_created_range(created_after, created_before)

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
    if isinstance(res, ListMessagesV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
