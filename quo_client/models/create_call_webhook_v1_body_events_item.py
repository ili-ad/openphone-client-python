from enum import Enum


class CreateCallWebhookV1BodyEventsItem(str, Enum):
    CALL_COMPLETED = "call.completed"
    CALL_RECORDING_COMPLETED = "call.recording.completed"
    CALL_RINGING = "call.ringing"

    def __str__(self) -> str:
        return str(self.value)
