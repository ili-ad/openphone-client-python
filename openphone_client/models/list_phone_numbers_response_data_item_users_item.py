from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListPhoneNumbersResponseDataItemUsersItem")


@_attrs_define
class ListPhoneNumbersResponseDataItemUsersItem:
    """
    Attributes:
        email (str):
        first_name (Union[None, str]):
        group_id (str):
        id (str):
        last_name (Union[None, str]):
        role (str):
    """

    email: str
    first_name: Union[None, str]
    group_id: str
    id: str
    last_name: Union[None, str]
    role: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name: Union[None, str]
        first_name = self.first_name

        group_id = self.group_id

        id = self.id

        last_name: Union[None, str]
        last_name = self.last_name

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "groupId": group_id,
                "id": id,
                "lastName": last_name,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_first_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        first_name = _parse_first_name(d.pop("firstName"))

        group_id = d.pop("groupId")

        id = d.pop("id")

        def _parse_last_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_name = _parse_last_name(d.pop("lastName"))

        role = d.pop("role")

        list_phone_numbers_response_data_item_users_item = cls(
            email=email,
            first_name=first_name,
            group_id=group_id,
            id=id,
            last_name=last_name,
            role=role,
        )

        list_phone_numbers_response_data_item_users_item.additional_properties = d
        return list_phone_numbers_response_data_item_users_item

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
