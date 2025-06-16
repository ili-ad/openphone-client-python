from enum import Enum


class SendMessageV1BodySetInboxStatus(str, Enum):
    DONE = "done"

    def __str__(self) -> str:
        return str(self.value)
