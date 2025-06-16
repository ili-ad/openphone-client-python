from enum import Enum


class GetWebhookByIdV1Response200DataType3EventsItem(str, Enum):
    CALL_TRANSCRIPT_COMPLETED = "call.transcript.completed"

    def __str__(self) -> str:
        return str(self.value)
