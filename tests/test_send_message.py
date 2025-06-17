import os
from httpx import Response

from openphone_client.models.send_message_v1_body import SendMessageV1Body


def test_send_message(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="POST",
        url="https://api.openphone.com/v1/messages",
        json={
            "data": {
                "id": "msg1",
                "to": ["+123"],
                "from": "+1555",
                "text": "hi",
                "phoneNumberId": None,
                "direction": "outgoing",
                "userId": "u1",
                "status": "queued",
                "createdAt": "2023-01-01T00:00:00Z",
                "updatedAt": "2023-01-01T00:00:00Z",
            }
        },
        status_code=202,
    )

    from openphone_sdk.send_message import send_message

    body = SendMessageV1Body(content="hi", from_="+1555", to=["+123"])
    out = send_message(body)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert str(req.url) == "https://api.openphone.com/v1/messages"
    assert req.headers.get("X-API-KEY") == "k"
    import json

    assert json.loads(req.content.decode()) == body.to_dict()
    assert out.data.id == "msg1"
