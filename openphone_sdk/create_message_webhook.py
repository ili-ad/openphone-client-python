from openphone_sdk.request import client
from openphone_client.api.webhooks.create_message_webhook_v_1 import sync
from openphone_client.models.create_message_webhook_v1_body import CreateMessageWebhookV1Body
from openphone_client.models.create_message_webhook_v1_response_201 import CreateMessageWebhookV1Response201


def create_message_webhook(body: CreateMessageWebhookV1Body) -> CreateMessageWebhookV1Response201:
    """Create a new webhook for messages and return it or raise RuntimeError on non-201."""
    res = sync(client=client(), body=body)
    if isinstance(res, CreateMessageWebhookV1Response201):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
