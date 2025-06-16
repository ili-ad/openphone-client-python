from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_phone_numbers_response_data_item_restrictions import ListPhoneNumbersResponseDataItemRestrictions
    from ..models.list_phone_numbers_response_data_item_users_item import ListPhoneNumbersResponseDataItemUsersItem


T = TypeVar("T", bound="ListPhoneNumbersResponseDataItem")


@_attrs_define
class ListPhoneNumbersResponseDataItem:
    """
    Attributes:
        id (str): The unique identifier of OpenPhone phone number.
        group_id (str): The unique identifier of the group to which the OpenPhone number belongs.
        created_at (str): Timestamp of when the phone number was added to the account in ISO 8601 format.
        updated_at (str): Timestamp of the last update to the phone number's details in ISO 8601 format.
        name (str): The display name of the phone number
        number (str): A phone number in E.164 format, including the country code.
        formatted_number (Union[None, str]):
        forward (Union[None, str]):
        port_request_id (Union[None, str]):
        porting_status (Union[None, str]):
        symbol (Union[None, str]):
        users (list['ListPhoneNumbersResponseDataItemUsersItem']):
        restrictions (ListPhoneNumbersResponseDataItemRestrictions):
    """

    id: str
    group_id: str
    created_at: str
    updated_at: str
    name: str
    number: str
    formatted_number: Union[None, str]
    forward: Union[None, str]
    port_request_id: Union[None, str]
    porting_status: Union[None, str]
    symbol: Union[None, str]
    users: list["ListPhoneNumbersResponseDataItemUsersItem"]
    restrictions: "ListPhoneNumbersResponseDataItemRestrictions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        group_id = self.group_id

        created_at = self.created_at

        updated_at = self.updated_at

        name = self.name

        number = self.number

        formatted_number: Union[None, str]
        formatted_number = self.formatted_number

        forward: Union[None, str]
        forward = self.forward

        port_request_id: Union[None, str]
        port_request_id = self.port_request_id

        porting_status: Union[None, str]
        porting_status = self.porting_status

        symbol: Union[None, str]
        symbol = self.symbol

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        restrictions = self.restrictions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "groupId": group_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "name": name,
                "number": number,
                "formattedNumber": formatted_number,
                "forward": forward,
                "portRequestId": port_request_id,
                "portingStatus": porting_status,
                "symbol": symbol,
                "users": users,
                "restrictions": restrictions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_phone_numbers_response_data_item_restrictions import (
            ListPhoneNumbersResponseDataItemRestrictions,
        )
        from ..models.list_phone_numbers_response_data_item_users_item import ListPhoneNumbersResponseDataItemUsersItem

        d = dict(src_dict)
        id = d.pop("id")

        group_id = d.pop("groupId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        name = d.pop("name")

        number = d.pop("number")

        def _parse_formatted_number(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        formatted_number = _parse_formatted_number(d.pop("formattedNumber"))

        def _parse_forward(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        forward = _parse_forward(d.pop("forward"))

        def _parse_port_request_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        port_request_id = _parse_port_request_id(d.pop("portRequestId"))

        def _parse_porting_status(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        porting_status = _parse_porting_status(d.pop("portingStatus"))

        def _parse_symbol(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        symbol = _parse_symbol(d.pop("symbol"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = ListPhoneNumbersResponseDataItemUsersItem.from_dict(users_item_data)

            users.append(users_item)

        restrictions = ListPhoneNumbersResponseDataItemRestrictions.from_dict(d.pop("restrictions"))

        list_phone_numbers_response_data_item = cls(
            id=id,
            group_id=group_id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            number=number,
            formatted_number=formatted_number,
            forward=forward,
            port_request_id=port_request_id,
            porting_status=porting_status,
            symbol=symbol,
            users=users,
            restrictions=restrictions,
        )

        list_phone_numbers_response_data_item.additional_properties = d
        return list_phone_numbers_response_data_item

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
