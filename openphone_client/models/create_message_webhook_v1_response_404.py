from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_message_webhook_v1_response_404_errors_item import CreateMessageWebhookV1Response404ErrorsItem


T = TypeVar("T", bound="CreateMessageWebhookV1Response404")


@_attrs_define
class CreateMessageWebhookV1Response404:
    """
    Attributes:
        message (str):
        code (Literal['0300404']):
        status (Literal[404]):
        docs (Literal['https://openphone.com/docs']):
        title (Literal['Not Found']):
        trace (Union[Unset, str]):
        errors (Union[Unset, list['CreateMessageWebhookV1Response404ErrorsItem']]):
    """

    message: str
    code: Literal["0300404"]
    status: Literal[404]
    docs: Literal["https://openphone.com/docs"]
    title: Literal["Not Found"]
    trace: Union[Unset, str] = UNSET
    errors: Union[Unset, list["CreateMessageWebhookV1Response404ErrorsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        code = self.code

        status = self.status

        docs = self.docs

        title = self.title

        trace = self.trace

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "code": code,
                "status": status,
                "docs": docs,
                "title": title,
            }
        )
        if trace is not UNSET:
            field_dict["trace"] = trace
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_message_webhook_v1_response_404_errors_item import (
            CreateMessageWebhookV1Response404ErrorsItem,
        )

        d = dict(src_dict)
        message = d.pop("message")

        code = cast(Literal["0300404"], d.pop("code"))
        if code != "0300404":
            raise ValueError(f"code must match const '0300404', got '{code}'")

        status = cast(Literal[404], d.pop("status"))
        if status != 404:
            raise ValueError(f"status must match const 404, got '{status}'")

        docs = cast(Literal["https://openphone.com/docs"], d.pop("docs"))
        if docs != "https://openphone.com/docs":
            raise ValueError(f"docs must match const 'https://openphone.com/docs', got '{docs}'")

        title = cast(Literal["Not Found"], d.pop("title"))
        if title != "Not Found":
            raise ValueError(f"title must match const 'Not Found', got '{title}'")

        trace = d.pop("trace", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = CreateMessageWebhookV1Response404ErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        create_message_webhook_v1_response_404 = cls(
            message=message,
            code=code,
            status=status,
            docs=docs,
            title=title,
            trace=trace,
            errors=errors,
        )

        create_message_webhook_v1_response_404.additional_properties = d
        return create_message_webhook_v1_response_404

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
