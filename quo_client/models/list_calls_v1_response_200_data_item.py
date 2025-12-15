import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.list_calls_v1_response_200_data_item_direction import ListCallsV1Response200DataItemDirection
from ..models.list_calls_v1_response_200_data_item_status import ListCallsV1Response200DataItemStatus

T = TypeVar("T", bound="ListCallsV1Response200DataItem")


@_attrs_define
class ListCallsV1Response200DataItem:
    """
    Attributes:
        answered_at (Union[None, datetime.datetime]):
        answered_by (Union[None, str]):
        initiated_by (Union[None, str]):
        direction (ListCallsV1Response200DataItemDirection): The direction of the call relative to the OpenPhone number.
        status (ListCallsV1Response200DataItemStatus): The current status of the call.
        completed_at (Union[None, datetime.datetime]):
        created_at (datetime.datetime): The timestamp when the call record was created, in ISO 8601 format.
        duration (int): The total duration of the call in seconds.
        forwarded_from (Union[None, str]):
        forwarded_to (Union[None, str]):
        id (str): The unique identifier of the call.
        phone_number_id (str): The unique identifier of the OpenPhone number associated with the call.
        participants (list[str]):
        updated_at (Union[None, datetime.datetime]):
        user_id (str): The unique identifier of the OpenPhone user account associated with the call.
    """

    answered_at: Union[None, datetime.datetime]
    answered_by: Union[None, str]
    initiated_by: Union[None, str]
    direction: ListCallsV1Response200DataItemDirection
    status: ListCallsV1Response200DataItemStatus
    completed_at: Union[None, datetime.datetime]
    created_at: datetime.datetime
    duration: int
    forwarded_from: Union[None, str]
    forwarded_to: Union[None, str]
    id: str
    phone_number_id: str
    participants: list[str]
    updated_at: Union[None, datetime.datetime]
    user_id: str

    def to_dict(self) -> dict[str, Any]:
        answered_at: Union[None, str]
        if isinstance(self.answered_at, datetime.datetime):
            answered_at = self.answered_at.isoformat()
        else:
            answered_at = self.answered_at

        answered_by: Union[None, str]
        answered_by = self.answered_by

        initiated_by: Union[None, str]
        initiated_by = self.initiated_by

        direction = self.direction.value

        status = self.status.value

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_at = self.created_at.isoformat()

        duration = self.duration

        forwarded_from: Union[None, str]
        forwarded_from = self.forwarded_from

        forwarded_to: Union[None, str]
        forwarded_to = self.forwarded_to

        id = self.id

        phone_number_id = self.phone_number_id

        participants = self.participants

        updated_at: Union[None, str]
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answeredAt": answered_at,
                "answeredBy": answered_by,
                "initiatedBy": initiated_by,
                "direction": direction,
                "status": status,
                "completedAt": completed_at,
                "createdAt": created_at,
                "duration": duration,
                "forwardedFrom": forwarded_from,
                "forwardedTo": forwarded_to,
                "id": id,
                "phoneNumberId": phone_number_id,
                "participants": participants,
                "updatedAt": updated_at,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_answered_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                answered_at_type_0 = isoparse(data)

                return answered_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        answered_at = _parse_answered_at(d.pop("answeredAt"))

        def _parse_answered_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        answered_by = _parse_answered_by(d.pop("answeredBy"))

        def _parse_initiated_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        initiated_by = _parse_initiated_by(d.pop("initiatedBy"))

        direction = ListCallsV1Response200DataItemDirection(d.pop("direction"))

        status = ListCallsV1Response200DataItemStatus(d.pop("status"))

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completedAt"))

        created_at = isoparse(d.pop("createdAt"))

        duration = d.pop("duration")

        def _parse_forwarded_from(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        forwarded_from = _parse_forwarded_from(d.pop("forwardedFrom"))

        def _parse_forwarded_to(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        forwarded_to = _parse_forwarded_to(d.pop("forwardedTo"))

        id = d.pop("id")

        phone_number_id = d.pop("phoneNumberId")

        participants = cast(list[str], d.pop("participants"))

        def _parse_updated_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        user_id = d.pop("userId")

        list_calls_v1_response_200_data_item = cls(
            answered_at=answered_at,
            answered_by=answered_by,
            initiated_by=initiated_by,
            direction=direction,
            status=status,
            completed_at=completed_at,
            created_at=created_at,
            duration=duration,
            forwarded_from=forwarded_from,
            forwarded_to=forwarded_to,
            id=id,
            phone_number_id=phone_number_id,
            participants=participants,
            updated_at=updated_at,
            user_id=user_id,
        )

        return list_calls_v1_response_200_data_item
