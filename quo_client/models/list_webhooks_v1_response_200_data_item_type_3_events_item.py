from enum import Enum


class ListWebhooksV1Response200DataItemType3EventsItem(str, Enum):
    CALL_TRANSCRIPT_COMPLETED = "call.transcript.completed"

    def __str__(self) -> str:
        return str(self.value)
