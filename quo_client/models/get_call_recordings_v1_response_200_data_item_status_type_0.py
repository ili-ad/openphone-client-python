from enum import Enum


class GetCallRecordingsV1Response200DataItemStatusType0(str, Enum):
    ABSENT = "absent"
    COMPLETED = "completed"
    DELETED = "deleted"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    PAUSED = "paused"
    PROCESSING = "processing"
    STOPPED = "stopped"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)
