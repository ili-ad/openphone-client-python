from quo_sdk.request import client
from quo_client.api.webhooks.list_webhooks_v_1 import sync
from quo_client.models.list_webhooks_v1_response_200 import ListWebhooksV1Response200
from quo_client.types import UNSET


def list_webhooks(user_id: str | None = None) -> ListWebhooksV1Response200:
    """Return webhooks for the authenticated workspace or raise RuntimeError on non-200."""
    res = sync(client=client(), user_id=user_id if user_id is not None else UNSET)
    if isinstance(res, ListWebhooksV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
