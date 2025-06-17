from openphone_sdk.request import client
from openphone_client.api.webhooks.create_call_transcript_webhook_v_1 import sync
from openphone_client.models.create_call_transcript_webhook_v1_body import CreateCallTranscriptWebhookV1Body
from openphone_client.models.create_call_transcript_webhook_v1_response_201 import CreateCallTranscriptWebhookV1Response201


def create_call_transcript_webhook(
    body: CreateCallTranscriptWebhookV1Body,
) -> CreateCallTranscriptWebhookV1Response201:
    """Create a new webhook for call transcripts and return the result or raise RuntimeError on failure."""
    res = sync(client=client(), body=body)
    if isinstance(res, CreateCallTranscriptWebhookV1Response201):
        return res
    raise RuntimeError(f"Unexpected response {type(res).__name__}")
