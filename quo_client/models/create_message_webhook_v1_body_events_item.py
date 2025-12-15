from enum import Enum


class CreateMessageWebhookV1BodyEventsItem(str, Enum):
    MESSAGE_DELIVERED = "message.delivered"
    MESSAGE_RECEIVED = "message.received"

    def __str__(self) -> str:
        return str(self.value)
