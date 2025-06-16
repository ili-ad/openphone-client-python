from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_contact_v1_response_201_data_default_fields_emails_item import (
        CreateContactV1Response201DataDefaultFieldsEmailsItem,
    )
    from ..models.create_contact_v1_response_201_data_default_fields_phone_numbers_item import (
        CreateContactV1Response201DataDefaultFieldsPhoneNumbersItem,
    )


T = TypeVar("T", bound="CreateContactV1Response201DataDefaultFields")


@_attrs_define
class CreateContactV1Response201DataDefaultFields:
    """
    Attributes:
        company (Union[None, str]):
        emails (list['CreateContactV1Response201DataDefaultFieldsEmailsItem']):
        first_name (Union[None, str]):
        last_name (Union[None, str]):
        phone_numbers (list['CreateContactV1Response201DataDefaultFieldsPhoneNumbersItem']):
        role (Union[None, str]):
    """

    company: Union[None, str]
    emails: list["CreateContactV1Response201DataDefaultFieldsEmailsItem"]
    first_name: Union[None, str]
    last_name: Union[None, str]
    phone_numbers: list["CreateContactV1Response201DataDefaultFieldsPhoneNumbersItem"]
    role: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company: Union[None, str]
        company = self.company

        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()
            emails.append(emails_item)

        first_name: Union[None, str]
        first_name = self.first_name

        last_name: Union[None, str]
        last_name = self.last_name

        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)

        role: Union[None, str]
        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "emails": emails,
                "firstName": first_name,
                "lastName": last_name,
                "phoneNumbers": phone_numbers,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_contact_v1_response_201_data_default_fields_emails_item import (
            CreateContactV1Response201DataDefaultFieldsEmailsItem,
        )
        from ..models.create_contact_v1_response_201_data_default_fields_phone_numbers_item import (
            CreateContactV1Response201DataDefaultFieldsPhoneNumbersItem,
        )

        d = dict(src_dict)

        def _parse_company(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        company = _parse_company(d.pop("company"))

        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = CreateContactV1Response201DataDefaultFieldsEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        def _parse_first_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        first_name = _parse_first_name(d.pop("firstName"))

        def _parse_last_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_name = _parse_last_name(d.pop("lastName"))

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = CreateContactV1Response201DataDefaultFieldsPhoneNumbersItem.from_dict(
                phone_numbers_item_data
            )

            phone_numbers.append(phone_numbers_item)

        def _parse_role(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        role = _parse_role(d.pop("role"))

        create_contact_v1_response_201_data_default_fields = cls(
            company=company,
            emails=emails,
            first_name=first_name,
            last_name=last_name,
            phone_numbers=phone_numbers,
            role=role,
        )

        create_contact_v1_response_201_data_default_fields.additional_properties = d
        return create_contact_v1_response_201_data_default_fields

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
