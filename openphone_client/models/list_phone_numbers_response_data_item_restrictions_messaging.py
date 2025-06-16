from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_phone_numbers_response_data_item_restrictions_messaging_ca import (
    ListPhoneNumbersResponseDataItemRestrictionsMessagingCA,
)
from ..models.list_phone_numbers_response_data_item_restrictions_messaging_intl import (
    ListPhoneNumbersResponseDataItemRestrictionsMessagingIntl,
)
from ..models.list_phone_numbers_response_data_item_restrictions_messaging_us import (
    ListPhoneNumbersResponseDataItemRestrictionsMessagingUS,
)

T = TypeVar("T", bound="ListPhoneNumbersResponseDataItemRestrictionsMessaging")


@_attrs_define
class ListPhoneNumbersResponseDataItemRestrictionsMessaging:
    """
    Attributes:
        ca (ListPhoneNumbersResponseDataItemRestrictionsMessagingCA): The phone-number usage restriction status for a
            specific region
        us (ListPhoneNumbersResponseDataItemRestrictionsMessagingUS): The phone-number usage restriction status for a
            specific region
        intl (ListPhoneNumbersResponseDataItemRestrictionsMessagingIntl): The phone-number usage restriction status for
            a specific region
    """

    ca: ListPhoneNumbersResponseDataItemRestrictionsMessagingCA
    us: ListPhoneNumbersResponseDataItemRestrictionsMessagingUS
    intl: ListPhoneNumbersResponseDataItemRestrictionsMessagingIntl
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ca = self.ca.value

        us = self.us.value

        intl = self.intl.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CA": ca,
                "US": us,
                "Intl": intl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ca = ListPhoneNumbersResponseDataItemRestrictionsMessagingCA(d.pop("CA"))

        us = ListPhoneNumbersResponseDataItemRestrictionsMessagingUS(d.pop("US"))

        intl = ListPhoneNumbersResponseDataItemRestrictionsMessagingIntl(d.pop("Intl"))

        list_phone_numbers_response_data_item_restrictions_messaging = cls(
            ca=ca,
            us=us,
            intl=intl,
        )

        list_phone_numbers_response_data_item_restrictions_messaging.additional_properties = d
        return list_phone_numbers_response_data_item_restrictions_messaging

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
