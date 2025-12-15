from enum import Enum


class GetWebhookByIdV1Response200DataType2Status(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
