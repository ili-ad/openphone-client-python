# docs/wrapper_example.py
import pytest; pytest.skip("template example – skipped while SDK is empty", allow_module_level=True)
from openphone_sdk.request import client
from openphone_client.api.calls.get_call_recordings_v_1 import sync
from openphone_client.models.get_call_recordings_v1_response_200 import (
    GetCallRecordingsV1Response200,
)

def get_call_recordings(call_id: str) -> GetCallRecordingsV1Response200:
    """Return recordings or raise RuntimeError on non-200."""
    res = sync(call_id=call_id, client=client())
    if isinstance(res, GetCallRecordingsV1Response200):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
