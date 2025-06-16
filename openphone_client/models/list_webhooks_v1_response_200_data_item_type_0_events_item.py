from enum import Enum


class ListWebhooksV1Response200DataItemType0EventsItem(str, Enum):
    MESSAGE_DELIVERED = "message.delivered"
    MESSAGE_RECEIVED = "message.received"

    def __str__(self) -> str:
        return str(self.value)
