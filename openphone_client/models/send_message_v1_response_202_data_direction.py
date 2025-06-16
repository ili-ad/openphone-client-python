from enum import Enum


class SendMessageV1Response202DataDirection(str, Enum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"

    def __str__(self) -> str:
        return str(self.value)
