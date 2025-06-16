from enum import Enum


class ListPhoneNumbersResponseDataItemRestrictionsCallingIntl(str, Enum):
    RESTRICTED = "restricted"
    UNRESTRICTED = "unrestricted"

    def __str__(self) -> str:
        return str(self.value)
