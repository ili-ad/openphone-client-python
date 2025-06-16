from enum import Enum


class ListPhoneNumbersResponseDataItemRestrictionsMessagingUS(str, Enum):
    RESTRICTED = "restricted"
    UNRESTRICTED = "unrestricted"

    def __str__(self) -> str:
        return str(self.value)
