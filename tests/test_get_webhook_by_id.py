import os
from httpx import Response


def test_get_webhook_by_id(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/webhooks/WH123",
        json={
            "data": {
                "id": "WH123",
                "userId": "U1",
                "orgId": "O1",
                "label": "Test",
                "status": "enabled",
                "url": "https://example.com",
                "key": "key",
                "createdAt": "2024-01-01T00:00:00Z",
                "updatedAt": "2024-01-01T00:00:00Z",
                "deletedAt": None,
                "events": ["call.transcript.completed"],
                "resourceIds": ["*"],
            }
        },
        status_code=200,
    )

    from quo_sdk.get_webhook_by_id import get_webhook_by_id

    out = get_webhook_by_id("WH123")

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/webhooks/WH123"
    assert req.headers.get("Authorization") == "k"
    assert out.data.id == "WH123"
