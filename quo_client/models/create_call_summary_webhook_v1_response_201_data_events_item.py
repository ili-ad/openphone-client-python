from enum import Enum


class CreateCallSummaryWebhookV1Response201DataEventsItem(str, Enum):
    CALL_SUMMARY_COMPLETED = "call.summary.completed"

    def __str__(self) -> str:
        return str(self.value)
