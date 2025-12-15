from enum import Enum


class GetContactCustomFieldsV1Response200DataItemType(str, Enum):
    ADDRESS = "address"
    BOOLEAN = "boolean"
    DATE = "date"
    MULTI_SELECT = "multi-select"
    NUMBER = "number"
    STRING = "string"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
