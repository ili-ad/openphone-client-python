from enum import Enum


class GetMessageByIdV1Response200DataStatus(str, Enum):
    DELIVERED = "delivered"
    QUEUED = "queued"
    SENT = "sent"
    UNDELIVERED = "undelivered"

    def __str__(self) -> str:
        return str(self.value)
