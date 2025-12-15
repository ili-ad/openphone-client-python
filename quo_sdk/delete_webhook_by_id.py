from quo_sdk.request import client
from quo_client.api.webhooks.delete_webhook_by_id_v_1 import sync


def delete_webhook_by_id(webhook_id: str) -> None:
    """Delete a webhook by ID or raise RuntimeError on non-204."""

    res = sync(id=webhook_id, client=client())
    if res is None:
        return None
    raise RuntimeError(f"Unexpected response {type(res).__name__}")

