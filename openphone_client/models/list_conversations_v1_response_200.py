from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_conversations_v1_response_200_data_item import ListConversationsV1Response200DataItem


T = TypeVar("T", bound="ListConversationsV1Response200")


@_attrs_define
class ListConversationsV1Response200:
    """
    Attributes:
        data (list['ListConversationsV1Response200DataItem']):
        total_items (int): Total number of items available. ⚠️ Note: `totalItems` is not accurately returning the total
            number of items that can be paginated. We are working on fixing this issue.
        next_page_token (Union[None, str]):
    """

    data: list["ListConversationsV1Response200DataItem"]
    total_items: int
    next_page_token: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        total_items = self.total_items

        next_page_token: Union[None, str]
        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "totalItems": total_items,
                "nextPageToken": next_page_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_conversations_v1_response_200_data_item import ListConversationsV1Response200DataItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListConversationsV1Response200DataItem.from_dict(data_item_data)

            data.append(data_item)

        total_items = d.pop("totalItems")

        def _parse_next_page_token(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken"))

        list_conversations_v1_response_200 = cls(
            data=data,
            total_items=total_items,
            next_page_token=next_page_token,
        )

        list_conversations_v1_response_200.additional_properties = d
        return list_conversations_v1_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
