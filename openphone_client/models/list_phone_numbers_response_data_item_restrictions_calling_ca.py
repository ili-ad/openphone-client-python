from enum import Enum


class ListPhoneNumbersResponseDataItemRestrictionsCallingCA(str, Enum):
    RESTRICTED = "restricted"
    UNRESTRICTED = "unrestricted"

    def __str__(self) -> str:
        return str(self.value)
