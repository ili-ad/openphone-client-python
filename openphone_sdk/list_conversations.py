from __future__ import annotations

import datetime
from typing import List, Optional

from openphone_sdk.request import client
from openphone_client.api.conversations.list_conversations_v_1 import sync
from openphone_client.models.list_conversations_v1_response_200 import ListConversationsV1Response200
from openphone_client.types import UNSET


def list_conversations(
    *,
    phone_number: Optional[str] = None,
    phone_numbers: Optional[List[str]] = None,
    user_id: Optional[str] = None,
    created_after: Optional[datetime.datetime] = None,
    created_before: Optional[datetime.datetime] = None,
    exclude_inactive: Optional[bool] = None,
    updated_after: Optional[datetime.datetime] = None,
    updated_before: Optional[datetime.datetime] = None,
    max_results: int = 10,
    page_token: Optional[str] = None,
) -> ListConversationsV1Response200:
    """Return conversations or raise RuntimeError on non-200."""
    res = sync(
        client=client(),
        phone_number=phone_number if phone_number is not None else UNSET,
        phone_numbers=phone_numbers if phone_numbers is not None else UNSET,
        user_id=user_id if user_id is not None else UNSET,
        created_after=created_after if created_after is not None else UNSET,
        created_before=created_before if created_before is not None else UNSET,
        exclude_inactive=exclude_inactive if exclude_inactive is not None else UNSET,
        updated_after=updated_after if updated_after is not None else UNSET,
        updated_before=updated_before if updated_before is not None else UNSET,
        max_results=max_results,
        page_token=page_token if page_token is not None else UNSET,
    )
    if isinstance(res, ListConversationsV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
