from enum import Enum


class ListWebhooksV1Response200DataItemType2EventsItem(str, Enum):
    CALL_SUMMARY_COMPLETED = "call.summary.completed"

    def __str__(self) -> str:
        return str(self.value)
