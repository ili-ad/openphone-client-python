from enum import Enum


class ListMessagesV1Response200DataItemStatus(str, Enum):
    DELIVERED = "delivered"
    QUEUED = "queued"
    SENT = "sent"
    UNDELIVERED = "undelivered"

    def __str__(self) -> str:
        return str(self.value)
