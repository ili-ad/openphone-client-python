from enum import Enum


class CreateCallTranscriptWebhookV1Response201DataEventsItem(str, Enum):
    CALL_TRANSCRIPT_COMPLETED = "call.transcript.completed"

    def __str__(self) -> str:
        return str(self.value)
