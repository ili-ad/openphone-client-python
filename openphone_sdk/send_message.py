from openphone_sdk.request import client
from openphone_client.api.messages.send_message_v_1 import sync
from openphone_client.models.send_message_v1_body import SendMessageV1Body
from openphone_client.models.send_message_v1_response_202 import SendMessageV1Response202


def send_message(body: SendMessageV1Body) -> SendMessageV1Response202:
    """Send a text message and return the response or raise RuntimeError."""
    res = sync(client=client(), body=body)
    if isinstance(res, SendMessageV1Response202):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
