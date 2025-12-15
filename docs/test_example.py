# docs/test_example.py
import pytest; pytest.skip("template example – skipped while SDK is empty", allow_module_level=True)
import os
from httpx import Response

def test_get_recordings(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/call-recordings/123",
        json={"data": []},
        status_code=200,
    )

    from quo_sdk.call_recordings_by_id import get_call_recordings
    out = get_call_recordings("123")
    assert out.data == []
