from quo_sdk.request import client
from quo_client.api.webhooks.create_call_webhook_v_1 import sync
from quo_client.models.create_call_webhook_v1_body import CreateCallWebhookV1Body
from quo_client.models.create_call_webhook_v1_response_201 import CreateCallWebhookV1Response201


def create_call_webhook(body: CreateCallWebhookV1Body) -> CreateCallWebhookV1Response201:
    """Create a new webhook for calls or raise RuntimeError on non-201."""
    res = sync(client=client(), body=body)
    if isinstance(res, CreateCallWebhookV1Response201):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
