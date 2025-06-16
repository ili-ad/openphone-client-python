from enum import Enum


class ListPhoneNumbersResponseDataItemRestrictionsMessagingIntl(str, Enum):
    RESTRICTED = "restricted"
    UNRESTRICTED = "unrestricted"

    def __str__(self) -> str:
        return str(self.value)
