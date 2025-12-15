from quo_sdk.request import client
from quo_client.api.phone_numbers.list_phone_numbers_v_1 import sync
from quo_client.types import UNSET
from quo_client.models.list_phone_numbers_response import ListPhoneNumbersResponse


def list_phone_numbers(user_id: str | None = None) -> ListPhoneNumbersResponse:
    """Return phone numbers for the workspace or a specific user."""
    res = sync(client=client(), user_id=user_id if user_id is not None else UNSET)
    if isinstance(res, ListPhoneNumbersResponse):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
