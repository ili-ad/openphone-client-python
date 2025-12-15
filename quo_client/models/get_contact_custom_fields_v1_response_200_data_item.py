from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_contact_custom_fields_v1_response_200_data_item_type import (
    GetContactCustomFieldsV1Response200DataItemType,
)

T = TypeVar("T", bound="GetContactCustomFieldsV1Response200DataItem")


@_attrs_define
class GetContactCustomFieldsV1Response200DataItem:
    """
    Attributes:
        name (str): The name of the custom contact field. This name is set by users in the OpenPhone interface when the
            custom field is created.
        key (str): The identifying key for contact custom field.
        type_ (GetContactCustomFieldsV1Response200DataItemType): The data type of the custom contact field, determining
            what kind of information can be stored and how it should be formatted.
    """

    name: str
    key: str
    type_: GetContactCustomFieldsV1Response200DataItemType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        key = self.key

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "key": key,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        key = d.pop("key")

        type_ = GetContactCustomFieldsV1Response200DataItemType(d.pop("type"))

        get_contact_custom_fields_v1_response_200_data_item = cls(
            name=name,
            key=key,
            type_=type_,
        )

        get_contact_custom_fields_v1_response_200_data_item.additional_properties = d
        return get_contact_custom_fields_v1_response_200_data_item

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
