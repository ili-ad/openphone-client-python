from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_contact_by_id_v1_body_default_fields_emails_item import (
        UpdateContactByIdV1BodyDefaultFieldsEmailsItem,
    )
    from ..models.update_contact_by_id_v1_body_default_fields_phone_numbers_item import (
        UpdateContactByIdV1BodyDefaultFieldsPhoneNumbersItem,
    )


T = TypeVar("T", bound="UpdateContactByIdV1BodyDefaultFields")


@_attrs_define
class UpdateContactByIdV1BodyDefaultFields:
    """
    Attributes:
        company (Union[None, Unset, str]):
        emails (Union[Unset, list['UpdateContactByIdV1BodyDefaultFieldsEmailsItem']]):
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        phone_numbers (Union[Unset, list['UpdateContactByIdV1BodyDefaultFieldsPhoneNumbersItem']]):
        role (Union[None, Unset, str]):
    """

    company: Union[None, Unset, str] = UNSET
    emails: Union[Unset, list["UpdateContactByIdV1BodyDefaultFieldsEmailsItem"]] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    phone_numbers: Union[Unset, list["UpdateContactByIdV1BodyDefaultFieldsPhoneNumbersItem"]] = UNSET
    role: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company: Union[None, Unset, str]
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        emails: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        phone_numbers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if emails is not UNSET:
            field_dict["emails"] = emails
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_contact_by_id_v1_body_default_fields_emails_item import (
            UpdateContactByIdV1BodyDefaultFieldsEmailsItem,
        )
        from ..models.update_contact_by_id_v1_body_default_fields_phone_numbers_item import (
            UpdateContactByIdV1BodyDefaultFieldsPhoneNumbersItem,
        )

        d = dict(src_dict)

        def _parse_company(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company = _parse_company(d.pop("company", UNSET))

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = UpdateContactByIdV1BodyDefaultFieldsEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = UpdateContactByIdV1BodyDefaultFieldsPhoneNumbersItem.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        update_contact_by_id_v1_body_default_fields = cls(
            company=company,
            emails=emails,
            first_name=first_name,
            last_name=last_name,
            phone_numbers=phone_numbers,
            role=role,
        )

        update_contact_by_id_v1_body_default_fields.additional_properties = d
        return update_contact_by_id_v1_body_default_fields

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
