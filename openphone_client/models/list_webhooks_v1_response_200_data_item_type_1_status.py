from enum import Enum


class ListWebhooksV1Response200DataItemType1Status(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
