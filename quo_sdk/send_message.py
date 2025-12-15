from quo_sdk.request import client
from quo_client.api.messages.send_message_v_1 import sync
from quo_client.models.send_message_v1_body import SendMessageV1Body
from quo_client.models.send_message_v1_response_202 import SendMessageV1Response202


def send_message(body: SendMessageV1Body) -> SendMessageV1Response202:
    """Send a text message and return the response or raise RuntimeError."""

    recipients = body.to
    if recipients is None or len(recipients) != 1:
        raise ValueError("send_message requires exactly one recipient in 'to'")

    res = sync(client=client(), body=body)
    if isinstance(res, SendMessageV1Response202):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
