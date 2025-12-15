from enum import Enum


class GetWebhookByIdV1Response200DataType2EventsItem(str, Enum):
    CALL_SUMMARY_COMPLETED = "call.summary.completed"

    def __str__(self) -> str:
        return str(self.value)
