import os
from httpx import Response

from quo_client.models.create_call_summary_webhook_v1_body import (
    CreateCallSummaryWebhookV1Body,
    CreateCallSummaryWebhookV1BodyEventsItem,
)


def test_create_call_summary_webhook(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    body = CreateCallSummaryWebhookV1Body(
        events=[CreateCallSummaryWebhookV1BodyEventsItem.CALL_SUMMARY_COMPLETED],
        url="https://example.com",
    )

    httpx_mock.add_response(
        method="POST",
        url="https://api.openphone.com/v1/webhooks/call-summaries",
        json={
            "data": {
                "id": "wh_1",
                "userId": "u1",
                "orgId": "o1",
                "label": None,
                "status": "enabled",
                "url": "https://example.com",
                "key": "k1",
                "createdAt": "2023-01-01T00:00:00Z",
                "updatedAt": "2023-01-01T00:00:00Z",
                "deletedAt": None,
                "events": ["call.summary.completed"],
                "resourceIds": ["*"],
            }
        },
        status_code=201,
    )

    from quo_sdk.create_call_summary_webhook import create_call_summary_webhook

    out = create_call_summary_webhook(body)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert str(req.url) == "https://api.openphone.com/v1/webhooks/call-summaries"
    assert req.headers.get("Authorization") == "k"
    import json

    assert json.loads(req.content.decode()) == body.to_dict()
    assert out.data.id == "wh_1"
