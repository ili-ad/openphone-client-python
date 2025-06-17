import os
from httpx import Response


def test_get_call_summary(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/call-summaries/AC123",
        json={
            "data": {
                "callId": "AC123",
                "nextSteps": [],
                "status": "completed",
                "summary": [],
                "jobs": [],
            }
        },
        status_code=200,
    )

    from openphone_sdk.get_call_summary import get_call_summary

    out = get_call_summary("AC123")

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/call-summaries/AC123"
    assert req.headers.get("X-API-KEY") == "k"
    assert out.data.call_id == "AC123"
