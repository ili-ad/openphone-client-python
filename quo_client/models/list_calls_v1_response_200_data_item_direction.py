from enum import Enum


class ListCallsV1Response200DataItemDirection(str, Enum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"

    def __str__(self) -> str:
        return str(self.value)
