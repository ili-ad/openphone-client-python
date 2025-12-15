from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateContactV1Response201DataCustomFieldsItem")


@_attrs_define
class CreateContactV1Response201DataCustomFieldsItem:
    """
    Attributes:
        name (str): The name of the custom contact field. This name is set by users in the OpenPhone interface when the
            custom field is created.
        key (Union[Unset, str]): The identifying key for contact custom field.
        id (Union[Unset, str]): The unique identifier for the contact custom field.
    """

    name: str
    key: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        key = self.key

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        key = d.pop("key", UNSET)

        id = d.pop("id", UNSET)

        create_contact_v1_response_201_data_custom_fields_item = cls(
            name=name,
            key=key,
            id=id,
        )

        create_contact_v1_response_201_data_custom_fields_item.additional_properties = d
        return create_contact_v1_response_201_data_custom_fields_item

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
