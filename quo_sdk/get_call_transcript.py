from quo_sdk.request import client
from quo_client.api.calls.get_call_transcript_v_1 import sync
from quo_client.models.get_call_transcript_v1_response_200 import (
    GetCallTranscriptV1Response200,
)


def get_call_transcript(call_id: str) -> GetCallTranscriptV1Response200:
    """Return transcript for the given call ID or raise RuntimeError on non-200."""
    res = sync(id=call_id, client=client())
    if isinstance(res, GetCallTranscriptV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
