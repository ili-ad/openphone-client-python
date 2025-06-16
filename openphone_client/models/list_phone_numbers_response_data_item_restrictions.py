from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_phone_numbers_response_data_item_restrictions_calling import (
        ListPhoneNumbersResponseDataItemRestrictionsCalling,
    )
    from ..models.list_phone_numbers_response_data_item_restrictions_messaging import (
        ListPhoneNumbersResponseDataItemRestrictionsMessaging,
    )


T = TypeVar("T", bound="ListPhoneNumbersResponseDataItemRestrictions")


@_attrs_define
class ListPhoneNumbersResponseDataItemRestrictions:
    """
    Attributes:
        messaging (ListPhoneNumbersResponseDataItemRestrictionsMessaging):
        calling (ListPhoneNumbersResponseDataItemRestrictionsCalling):
    """

    messaging: "ListPhoneNumbersResponseDataItemRestrictionsMessaging"
    calling: "ListPhoneNumbersResponseDataItemRestrictionsCalling"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messaging = self.messaging.to_dict()

        calling = self.calling.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messaging": messaging,
                "calling": calling,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_phone_numbers_response_data_item_restrictions_calling import (
            ListPhoneNumbersResponseDataItemRestrictionsCalling,
        )
        from ..models.list_phone_numbers_response_data_item_restrictions_messaging import (
            ListPhoneNumbersResponseDataItemRestrictionsMessaging,
        )

        d = dict(src_dict)
        messaging = ListPhoneNumbersResponseDataItemRestrictionsMessaging.from_dict(d.pop("messaging"))

        calling = ListPhoneNumbersResponseDataItemRestrictionsCalling.from_dict(d.pop("calling"))

        list_phone_numbers_response_data_item_restrictions = cls(
            messaging=messaging,
            calling=calling,
        )

        list_phone_numbers_response_data_item_restrictions.additional_properties = d
        return list_phone_numbers_response_data_item_restrictions

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
