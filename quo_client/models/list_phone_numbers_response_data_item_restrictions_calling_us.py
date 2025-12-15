from enum import Enum


class ListPhoneNumbersResponseDataItemRestrictionsCallingUS(str, Enum):
    RESTRICTED = "restricted"
    UNRESTRICTED = "unrestricted"

    def __str__(self) -> str:
        return str(self.value)
