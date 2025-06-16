from enum import Enum


class CreateMessageWebhookV1Response201DataEventsItem(str, Enum):
    MESSAGE_DELIVERED = "message.delivered"
    MESSAGE_RECEIVED = "message.received"

    def __str__(self) -> str:
        return str(self.value)
