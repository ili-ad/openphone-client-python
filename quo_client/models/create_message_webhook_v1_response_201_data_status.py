from enum import Enum


class CreateMessageWebhookV1Response201DataStatus(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
