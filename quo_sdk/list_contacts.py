from quo_client.api.contacts.list_contacts_v_1 import sync
from quo_client.models.list_contacts_v1_response_200 import ListContactsV1Response200
from quo_client.types import UNSET, Unset
from quo_sdk.request import client


def list_contacts(*, external_ids: list[str], sources: list[str] | Unset = UNSET, max_results: int = 10, page_token: str | Unset = UNSET) -> ListContactsV1Response200:
    """Return contacts matching provided external IDs or raise RuntimeError on non-200."""
    res = sync(client=client(), external_ids=external_ids, sources=sources, max_results=max_results, page_token=page_token)
    if isinstance(res, ListContactsV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
