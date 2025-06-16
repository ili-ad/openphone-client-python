import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_message_by_id_v1_response_200_data_direction import GetMessageByIdV1Response200DataDirection
from ..models.get_message_by_id_v1_response_200_data_status import GetMessageByIdV1Response200DataStatus

T = TypeVar("T", bound="GetMessageByIdV1Response200Data")


@_attrs_define
class GetMessageByIdV1Response200Data:
    """
    Attributes:
        id (str): The unique identifier of the message.
        to (list[str]):
        from_ (str): A phone number in E.164 format, including the country code.
        text (str): The content of the message.
        phone_number_id (Union[None, str]):
        direction (GetMessageByIdV1Response200DataDirection): The direction of the message relative to the OpenPhone
            number.
        user_id (str): The unique identifier of the user who sent the message. Null for incoming messages.
        status (GetMessageByIdV1Response200DataStatus): The status of the message.
        created_at (datetime.datetime): The timestamp when the message was created at, in ISO 8601 format
        updated_at (datetime.datetime): The timestamp when the message status was last updated, in ISO 8601 format.
    """

    id: str
    to: list[str]
    from_: str
    text: str
    phone_number_id: Union[None, str]
    direction: GetMessageByIdV1Response200DataDirection
    user_id: str
    status: GetMessageByIdV1Response200DataStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        to = self.to

        from_ = self.from_

        text = self.text

        phone_number_id: Union[None, str]
        phone_number_id = self.phone_number_id

        direction = self.direction.value

        user_id = self.user_id

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "to": to,
                "from": from_,
                "text": text,
                "phoneNumberId": phone_number_id,
                "direction": direction,
                "userId": user_id,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        to = cast(list[str], d.pop("to"))

        from_ = d.pop("from")

        text = d.pop("text")

        def _parse_phone_number_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        phone_number_id = _parse_phone_number_id(d.pop("phoneNumberId"))

        direction = GetMessageByIdV1Response200DataDirection(d.pop("direction"))

        user_id = d.pop("userId")

        status = GetMessageByIdV1Response200DataStatus(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        get_message_by_id_v1_response_200_data = cls(
            id=id,
            to=to,
            from_=from_,
            text=text,
            phone_number_id=phone_number_id,
            direction=direction,
            user_id=user_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_message_by_id_v1_response_200_data.additional_properties = d
        return get_message_by_id_v1_response_200_data

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
