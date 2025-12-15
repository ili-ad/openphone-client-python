import os
from httpx import Response


def test_get_message_by_id(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="GET",
        url="https://api.openphone.com/v1/messages/MSG123",
        json={
            "data": {
                "id": "MSG123",
                "to": ["+10000000000"],
                "from": "+19999999999",
                "text": "hello",
                "phoneNumberId": None,
                "direction": "incoming",
                "userId": "USR1",
                "status": "sent",
                "createdAt": "2023-01-01T00:00:00Z",
                "updatedAt": "2023-01-01T00:00:00Z"
            }
        },
        status_code=200,
    )

    from openphone_sdk.get_message_by_id import get_message_by_id

    out = get_message_by_id("MSG123")

    req = httpx_mock.get_request()
    assert req.method == "GET"
    assert str(req.url) == "https://api.openphone.com/v1/messages/MSG123"
    assert req.headers.get("Authorization") == "k"
    assert out.data.id == "MSG123"
