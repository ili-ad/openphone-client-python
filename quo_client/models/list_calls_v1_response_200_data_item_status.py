from enum import Enum


class ListCallsV1Response200DataItemStatus(str, Enum):
    ABANDONED = "abandoned"
    ANSWERED = "answered"
    BUSY = "busy"
    CANCELED = "canceled"
    COMPLETED = "completed"
    FAILED = "failed"
    FORWARDED = "forwarded"
    INITIATED = "initiated"
    IN_PROGRESS = "in-progress"
    MISSED = "missed"
    NO_ANSWER = "no-answer"
    QUEUED = "queued"
    RINGING = "ringing"

    def __str__(self) -> str:
        return str(self.value)
