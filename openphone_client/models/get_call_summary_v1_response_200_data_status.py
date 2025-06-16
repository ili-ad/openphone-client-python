from enum import Enum


class GetCallSummaryV1Response200DataStatus(str, Enum):
    ABSENT = "absent"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"

    def __str__(self) -> str:
        return str(self.value)
