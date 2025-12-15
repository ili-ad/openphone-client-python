from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_contacts_v1_response_400_errors_item_schema import ListContactsV1Response400ErrorsItemSchema


T = TypeVar("T", bound="ListContactsV1Response400ErrorsItem")


@_attrs_define
class ListContactsV1Response400ErrorsItem:
    """
    Attributes:
        path (str):
        message (str):
        schema (ListContactsV1Response400ErrorsItemSchema):
        value (Union[Unset, Any]):
    """

    path: str
    message: str
    schema: "ListContactsV1Response400ErrorsItemSchema"
    value: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        message = self.message

        schema = self.schema.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "message": message,
                "schema": schema,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_contacts_v1_response_400_errors_item_schema import ListContactsV1Response400ErrorsItemSchema

        d = dict(src_dict)
        path = d.pop("path")

        message = d.pop("message")

        schema = ListContactsV1Response400ErrorsItemSchema.from_dict(d.pop("schema"))

        value = d.pop("value", UNSET)

        list_contacts_v1_response_400_errors_item = cls(
            path=path,
            message=message,
            schema=schema,
            value=value,
        )

        list_contacts_v1_response_400_errors_item.additional_properties = d
        return list_contacts_v1_response_400_errors_item

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
