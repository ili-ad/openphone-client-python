import os
from httpx import Response


def test_get_call_transcript(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/call-transcripts/AC123",
        json={
            "data": {
                "callId": "AC123",
                "createdAt": "2023-01-01T00:00:00Z",
                "dialogue": None,
                "duration": 1.0,
                "status": "completed",
            }
        },
        status_code=200,
    )

    from quo_sdk.get_call_transcript import get_call_transcript

    out = get_call_transcript("AC123")

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/call-transcripts/AC123"
    assert req.headers.get("Authorization") == "k"
    assert out.data.call_id == "AC123"
    assert out.data.status.value == "completed"
