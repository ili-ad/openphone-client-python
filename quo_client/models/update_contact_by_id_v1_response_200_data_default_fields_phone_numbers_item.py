from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateContactByIdV1Response200DataDefaultFieldsPhoneNumbersItem")


@_attrs_define
class UpdateContactByIdV1Response200DataDefaultFieldsPhoneNumbersItem:
    """
    Attributes:
        name (str): The name of the contact's phone number.
        value (Union[None, str]):
        id (Union[Unset, str]): The unique identifier of the contact phone number field.
    """

    name: str
    value: Union[None, str]
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value: Union[None, str]
        value = self.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_value(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        value = _parse_value(d.pop("value"))

        id = d.pop("id", UNSET)

        update_contact_by_id_v1_response_200_data_default_fields_phone_numbers_item = cls(
            name=name,
            value=value,
            id=id,
        )

        update_contact_by_id_v1_response_200_data_default_fields_phone_numbers_item.additional_properties = d
        return update_contact_by_id_v1_response_200_data_default_fields_phone_numbers_item

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
