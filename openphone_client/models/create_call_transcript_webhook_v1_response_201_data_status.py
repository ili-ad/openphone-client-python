from enum import Enum


class CreateCallTranscriptWebhookV1Response201DataStatus(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
