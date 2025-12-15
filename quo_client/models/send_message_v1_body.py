from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_message_v1_body_set_inbox_status import SendMessageV1BodySetInboxStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageV1Body")


@_attrs_define
class SendMessageV1Body:
    """
    Attributes:
        content (str): The text content of the message to be sent.
        from_ (str):
        to (list[str]):
        phone_number_id (Union[Unset, str]): DEPRECATED, use "from" instead. OpenPhone phone number ID to send a message
            from
        user_id (Union[Unset, str]): The unique identifier of the OpenPhone user sending the message. If not provided,
            defaults to the phone number owner.
        set_inbox_status (Union[Unset, SendMessageV1BodySetInboxStatus]): Used to set the status of the related
            OpenPhone inbox conversation. The default behavior without setting this parameter will be for the message sent
            to show up as an open conversation in the user's inbox. Setting the parameter to `'done'` would move the
            conversation to the Done inbox view.
    """

    content: str
    from_: str
    to: list[str]
    phone_number_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    set_inbox_status: Union[Unset, SendMessageV1BodySetInboxStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        from_: str
        from_ = self.from_

        to = self.to

        phone_number_id = self.phone_number_id

        user_id = self.user_id

        set_inbox_status: Union[Unset, str] = UNSET
        if not isinstance(self.set_inbox_status, Unset):
            set_inbox_status = self.set_inbox_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "from": from_,
                "to": to,
            }
        )
        if phone_number_id is not UNSET:
            field_dict["phoneNumberId"] = phone_number_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if set_inbox_status is not UNSET:
            field_dict["setInboxStatus"] = set_inbox_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        def _parse_from_(data: object) -> str:
            return cast(str, data)

        from_ = _parse_from_(d.pop("from"))

        to = cast(list[str], d.pop("to"))

        phone_number_id = d.pop("phoneNumberId", UNSET)

        user_id = d.pop("userId", UNSET)

        _set_inbox_status = d.pop("setInboxStatus", UNSET)
        set_inbox_status: Union[Unset, SendMessageV1BodySetInboxStatus]
        if isinstance(_set_inbox_status, Unset):
            set_inbox_status = UNSET
        else:
            set_inbox_status = SendMessageV1BodySetInboxStatus(_set_inbox_status)

        send_message_v1_body = cls(
            content=content,
            from_=from_,
            to=to,
            phone_number_id=phone_number_id,
            user_id=user_id,
            set_inbox_status=set_inbox_status,
        )

        send_message_v1_body.additional_properties = d
        return send_message_v1_body

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
