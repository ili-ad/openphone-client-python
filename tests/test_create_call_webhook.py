import os

from quo_client.models.create_call_webhook_v1_body import CreateCallWebhookV1Body
from quo_client.models.create_call_webhook_v1_body_events_item import CreateCallWebhookV1BodyEventsItem


def test_create_call_webhook(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="POST",
        url="https://api.openphone.com/v1/webhooks/calls",
        json={
            "data": {
                "id": "WH1",
                "userId": "U1",
                "orgId": "O1",
                "label": "test",
                "status": "enabled",
                "url": "https://example.com",
                "key": "abc",
                "createdAt": "2023-01-01T00:00:00Z",
                "updatedAt": "2023-01-01T00:00:00Z",
                "deletedAt": None,
                "events": ["call.completed"],
                "resourceIds": ["*"]
            }
        },
        status_code=201,
    )

    from quo_sdk.create_call_webhook import create_call_webhook

    body = CreateCallWebhookV1Body(
        url="https://example.com",
        events=[CreateCallWebhookV1BodyEventsItem.CALL_COMPLETED],
    )

    out = create_call_webhook(body)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert str(req.url) == "https://api.openphone.com/v1/webhooks/calls"
    assert req.headers.get("Authorization") == "k"

    import json

    assert json.loads(req.content.decode()) == {
        "url": "https://example.com",
        "events": ["call.completed"],
        "status": "enabled",
    }
    assert out.data.id == "WH1"
