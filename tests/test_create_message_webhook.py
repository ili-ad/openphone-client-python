import os
import datetime
from quo_client.models.create_message_webhook_v1_body import CreateMessageWebhookV1Body
from quo_client.models.create_message_webhook_v1_body_events_item import CreateMessageWebhookV1BodyEventsItem
from quo_client.models.create_message_webhook_v1_response_201 import CreateMessageWebhookV1Response201
from quo_client.models.create_message_webhook_v1_response_201_data import CreateMessageWebhookV1Response201Data
from quo_client.models.create_message_webhook_v1_response_201_data_events_item import (
    CreateMessageWebhookV1Response201DataEventsItem,
)
from quo_client.models.create_message_webhook_v1_response_201_data_status import (
    CreateMessageWebhookV1Response201DataStatus,
)


def test_create_message_webhook(httpx_mock):
    os.environ["OPENPHONE_API_KEY"] = "k"
    os.environ["OPENPHONE_BASE_URL"] = "https://api.openphone.com"

    body = CreateMessageWebhookV1Body(
        events=[CreateMessageWebhookV1BodyEventsItem.MESSAGE_RECEIVED],
        url="https://example.com/hook",
    )

    response_body = CreateMessageWebhookV1Response201(
        data=CreateMessageWebhookV1Response201Data(
            id="wh_123",
            user_id="u1",
            org_id="o1",
            label=None,
            status=CreateMessageWebhookV1Response201DataStatus.ENABLED,
            url="https://example.com/hook",
            key="key",
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            deleted_at=None,
            events=[CreateMessageWebhookV1Response201DataEventsItem.MESSAGE_RECEIVED],
            resource_ids=["*"]
        )
    )

    httpx_mock.add_response(
        method="POST",
        url="https://api.openphone.com/v1/webhooks/messages",
        json=response_body.to_dict(),
        status_code=201,
    )

    from quo_sdk.create_message_webhook import create_message_webhook

    out = create_message_webhook(body)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert str(req.url) == "https://api.openphone.com/v1/webhooks/messages"
    assert req.headers.get("Authorization") == "k"
    assert req.headers.get("Content-Type") == "application/json"
    import json
    assert json.loads(req.content.decode()) == body.to_dict()
    assert isinstance(out, CreateMessageWebhookV1Response201)
