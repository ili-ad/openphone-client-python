import os
import json


def test_create_call_transcript_webhook(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"
    httpx_mock.add_response(
        method="POST",
        url="https://api.openphone.com/v1/webhooks/call-transcripts",
        json={
            "data": {
                "id": "wh_1",
                "userId": "u",
                "orgId": "o",
                "label": None,
                "status": "enabled",
                "url": "https://example.com",
                "key": "k1",
                "createdAt": "2024-01-01T00:00:00Z",
                "updatedAt": "2024-01-01T00:00:00Z",
                "deletedAt": None,
                "events": ["call.transcript.completed"],
                "resourceIds": ["*"],
            }
        },
        status_code=201,
    )

    from openphone_client.models.create_call_transcript_webhook_v1_body import (
        CreateCallTranscriptWebhookV1Body,
        CreateCallTranscriptWebhookV1BodyEventsItem,
    )
    from openphone_sdk.create_call_transcript_webhook import create_call_transcript_webhook

    body = CreateCallTranscriptWebhookV1Body(
        events=[CreateCallTranscriptWebhookV1BodyEventsItem.CALL_TRANSCRIPT_COMPLETED],
        url="https://example.com",
    )

    out = create_call_transcript_webhook(body)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert str(req.url) == "https://api.openphone.com/v1/webhooks/call-transcripts"
    assert req.headers.get("X-API-KEY") == "k"
    body_json = json.loads(req.content.decode())
    assert body_json == {"events": ["call.transcript.completed"], "url": "https://example.com"}
    assert out.data.id == "wh_1"
