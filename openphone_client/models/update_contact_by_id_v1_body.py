from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_contact_by_id_v1_body_custom_fields_item import UpdateContactByIdV1BodyCustomFieldsItem
    from ..models.update_contact_by_id_v1_body_default_fields import UpdateContactByIdV1BodyDefaultFields


T = TypeVar("T", bound="UpdateContactByIdV1Body")


@_attrs_define
class UpdateContactByIdV1Body:
    """
    Attributes:
        external_id (Union[None, Unset, str]):
        source (Union[None, Unset, str]):
        source_url (Union[None, Unset, str]):
        default_fields (Union[Unset, UpdateContactByIdV1BodyDefaultFields]):
        custom_fields (Union[Unset, list['UpdateContactByIdV1BodyCustomFieldsItem']]):
    """

    external_id: Union[None, Unset, str] = UNSET
    source: Union[None, Unset, str] = UNSET
    source_url: Union[None, Unset, str] = UNSET
    default_fields: Union[Unset, "UpdateContactByIdV1BodyDefaultFields"] = UNSET
    custom_fields: Union[Unset, list["UpdateContactByIdV1BodyCustomFieldsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        source_url: Union[None, Unset, str]
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        default_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_fields, Unset):
            default_fields = self.default_fields.to_dict()

        custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if source is not UNSET:
            field_dict["source"] = source
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if default_fields is not UNSET:
            field_dict["defaultFields"] = default_fields
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_contact_by_id_v1_body_custom_fields_item import UpdateContactByIdV1BodyCustomFieldsItem
        from ..models.update_contact_by_id_v1_body_default_fields import UpdateContactByIdV1BodyDefaultFields

        d = dict(src_dict)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_source_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_url = _parse_source_url(d.pop("sourceUrl", UNSET))

        _default_fields = d.pop("defaultFields", UNSET)
        default_fields: Union[Unset, UpdateContactByIdV1BodyDefaultFields]
        if isinstance(_default_fields, Unset):
            default_fields = UNSET
        else:
            default_fields = UpdateContactByIdV1BodyDefaultFields.from_dict(_default_fields)

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = UpdateContactByIdV1BodyCustomFieldsItem.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        update_contact_by_id_v1_body = cls(
            external_id=external_id,
            source=source,
            source_url=source_url,
            default_fields=default_fields,
            custom_fields=custom_fields,
        )

        update_contact_by_id_v1_body.additional_properties = d
        return update_contact_by_id_v1_body

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
