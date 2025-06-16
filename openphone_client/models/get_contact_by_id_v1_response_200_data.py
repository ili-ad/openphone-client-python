import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_contact_by_id_v1_response_200_data_custom_fields_item import (
        GetContactByIdV1Response200DataCustomFieldsItem,
    )
    from ..models.get_contact_by_id_v1_response_200_data_default_fields import (
        GetContactByIdV1Response200DataDefaultFields,
    )


T = TypeVar("T", bound="GetContactByIdV1Response200Data")


@_attrs_define
class GetContactByIdV1Response200Data:
    """
    Attributes:
        id (str): The unique identifier of the contact.
        external_id (Union[None, str]):
        source (Union[None, str]):
        source_url (Union[None, str]):
        default_fields (GetContactByIdV1Response200DataDefaultFields):
        custom_fields (list['GetContactByIdV1Response200DataCustomFieldsItem']):
        created_at (datetime.datetime): Timestamp of contact creation in ISO 8601 format.
        updated_at (datetime.datetime): Timestamp of last contact update in ISO 8601 format.
        created_by_user_id (str): The unique identifier of the user who created the contact.
    """

    id: str
    external_id: Union[None, str]
    source: Union[None, str]
    source_url: Union[None, str]
    default_fields: "GetContactByIdV1Response200DataDefaultFields"
    custom_fields: list["GetContactByIdV1Response200DataCustomFieldsItem"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by_user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id: Union[None, str]
        external_id = self.external_id

        source: Union[None, str]
        source = self.source

        source_url: Union[None, str]
        source_url = self.source_url

        default_fields = self.default_fields.to_dict()

        custom_fields = []
        for custom_fields_item_data in self.custom_fields:
            custom_fields_item = custom_fields_item_data.to_dict()
            custom_fields.append(custom_fields_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by_user_id = self.created_by_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "externalId": external_id,
                "source": source,
                "sourceUrl": source_url,
                "defaultFields": default_fields,
                "customFields": custom_fields,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "createdByUserId": created_by_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_contact_by_id_v1_response_200_data_custom_fields_item import (
            GetContactByIdV1Response200DataCustomFieldsItem,
        )
        from ..models.get_contact_by_id_v1_response_200_data_default_fields import (
            GetContactByIdV1Response200DataDefaultFields,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_external_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_id = _parse_external_id(d.pop("externalId"))

        def _parse_source(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source = _parse_source(d.pop("source"))

        def _parse_source_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source_url = _parse_source_url(d.pop("sourceUrl"))

        default_fields = GetContactByIdV1Response200DataDefaultFields.from_dict(d.pop("defaultFields"))

        custom_fields = []
        _custom_fields = d.pop("customFields")
        for custom_fields_item_data in _custom_fields:
            custom_fields_item = GetContactByIdV1Response200DataCustomFieldsItem.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        created_by_user_id = d.pop("createdByUserId")

        get_contact_by_id_v1_response_200_data = cls(
            id=id,
            external_id=external_id,
            source=source,
            source_url=source_url,
            default_fields=default_fields,
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
        )

        get_contact_by_id_v1_response_200_data.additional_properties = d
        return get_contact_by_id_v1_response_200_data

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
