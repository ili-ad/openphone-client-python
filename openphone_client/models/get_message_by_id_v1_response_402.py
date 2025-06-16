from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_message_by_id_v1_response_402_errors_item import GetMessageByIdV1Response402ErrorsItem


T = TypeVar("T", bound="GetMessageByIdV1Response402")


@_attrs_define
class GetMessageByIdV1Response402:
    """
    Attributes:
        message (str):
        code (Literal['0200402']):
        status (Literal[402]):
        docs (Literal['https://openphone.com/docs']):
        title (Literal['Not Enough Credits']):
        description (Literal['The organization does not have enough prepaid credits to send the message']):
        trace (Union[Unset, str]):
        errors (Union[Unset, list['GetMessageByIdV1Response402ErrorsItem']]):
    """

    message: str
    code: Literal["0200402"]
    status: Literal[402]
    docs: Literal["https://openphone.com/docs"]
    title: Literal["Not Enough Credits"]
    description: Literal["The organization does not have enough prepaid credits to send the message"]
    trace: Union[Unset, str] = UNSET
    errors: Union[Unset, list["GetMessageByIdV1Response402ErrorsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        code = self.code

        status = self.status

        docs = self.docs

        title = self.title

        description = self.description

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
                "description": description,
            }
        )
        if trace is not UNSET:
            field_dict["trace"] = trace
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_message_by_id_v1_response_402_errors_item import GetMessageByIdV1Response402ErrorsItem

        d = dict(src_dict)
        message = d.pop("message")

        code = cast(Literal["0200402"], d.pop("code"))
        if code != "0200402":
            raise ValueError(f"code must match const '0200402', got '{code}'")

        status = cast(Literal[402], d.pop("status"))
        if status != 402:
            raise ValueError(f"status must match const 402, got '{status}'")

        docs = cast(Literal["https://openphone.com/docs"], d.pop("docs"))
        if docs != "https://openphone.com/docs":
            raise ValueError(f"docs must match const 'https://openphone.com/docs', got '{docs}'")

        title = cast(Literal["Not Enough Credits"], d.pop("title"))
        if title != "Not Enough Credits":
            raise ValueError(f"title must match const 'Not Enough Credits', got '{title}'")

        description = cast(
            Literal["The organization does not have enough prepaid credits to send the message"], d.pop("description")
        )
        if description != "The organization does not have enough prepaid credits to send the message":
            raise ValueError(
                f"description must match const 'The organization does not have enough prepaid credits to send the message', got '{description}'"
            )

        trace = d.pop("trace", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = GetMessageByIdV1Response402ErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        get_message_by_id_v1_response_402 = cls(
            message=message,
            code=code,
            status=status,
            docs=docs,
            title=title,
            description=description,
            trace=trace,
            errors=errors,
        )

        get_message_by_id_v1_response_402.additional_properties = d
        return get_message_by_id_v1_response_402

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
