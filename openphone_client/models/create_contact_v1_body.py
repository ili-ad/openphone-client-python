from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_contact_v1_body_custom_fields_item import CreateContactV1BodyCustomFieldsItem
    from ..models.create_contact_v1_body_default_fields import CreateContactV1BodyDefaultFields


T = TypeVar("T", bound="CreateContactV1Body")


@_attrs_define
class CreateContactV1Body:
    """
    Attributes:
        default_fields (CreateContactV1BodyDefaultFields):
        custom_fields (Union[Unset, list['CreateContactV1BodyCustomFieldsItem']]):
        created_by_user_id (Union[Unset, str]): The unique identifier of the user who created the contact.
        source (Union[Unset, str]): The contact's source. Defaults to `null` for contacts created in the UI. Defaults to
            `public-api` for contacts created via the public API. Cannot be one of the following reserved words:
            `openphone`, `device`, `csv`, `zapier`, `google-people`, `other` or start with one of the following reserved
            prefixes: `openphone`, `csv`. Default: 'public-api'.
        source_url (Union[Unset, str]): A link to the contact in the source system.
        external_id (Union[None, Unset, str]):
    """

    default_fields: "CreateContactV1BodyDefaultFields"
    custom_fields: Union[Unset, list["CreateContactV1BodyCustomFieldsItem"]] = UNSET
    created_by_user_id: Union[Unset, str] = UNSET
    source: Union[Unset, str] = "public-api"
    source_url: Union[Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_fields = self.default_fields.to_dict()

        custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        created_by_user_id = self.created_by_user_id

        source = self.source

        source_url = self.source_url

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultFields": default_fields,
            }
        )
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if source is not UNSET:
            field_dict["source"] = source
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_contact_v1_body_custom_fields_item import CreateContactV1BodyCustomFieldsItem
        from ..models.create_contact_v1_body_default_fields import CreateContactV1BodyDefaultFields

        d = dict(src_dict)
        default_fields = CreateContactV1BodyDefaultFields.from_dict(d.pop("defaultFields"))

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CreateContactV1BodyCustomFieldsItem.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        created_by_user_id = d.pop("createdByUserId", UNSET)

        source = d.pop("source", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        create_contact_v1_body = cls(
            default_fields=default_fields,
            custom_fields=custom_fields,
            created_by_user_id=created_by_user_id,
            source=source,
            source_url=source_url,
            external_id=external_id,
        )

        create_contact_v1_body.additional_properties = d
        return create_contact_v1_body

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
