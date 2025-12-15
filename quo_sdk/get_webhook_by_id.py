from quo_sdk.request import client
from quo_client.api.webhooks.get_webhook_by_id_v_1 import sync
from quo_client.models.get_webhook_by_id_v1_response_200 import GetWebhookByIdV1Response200


def get_webhook_by_id(id: str) -> GetWebhookByIdV1Response200:
    """Return a webhook by ID or raise RuntimeError on non-200."""
    res = sync(id=id, client=client())
    if isinstance(res, GetWebhookByIdV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
