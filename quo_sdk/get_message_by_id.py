from quo_sdk.request import client
from quo_client.api.messages.get_message_by_id_v_1 import sync
from quo_client.models.get_message_by_id_v1_response_200 import GetMessageByIdV1Response200


def get_message_by_id(message_id: str) -> GetMessageByIdV1Response200:
    """Return a message by ID or raise RuntimeError on non-200."""
    res = sync(id=message_id, client=client())
    if isinstance(res, GetMessageByIdV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
