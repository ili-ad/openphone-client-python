from enum import Enum


class ListWebhooksV1Response200DataItemType1EventsItem(str, Enum):
    CALL_COMPLETED = "call.completed"
    CALL_RECORDING_COMPLETED = "call.recording.completed"
    CALL_RINGING = "call.ringing"

    def __str__(self) -> str:
        return str(self.value)
