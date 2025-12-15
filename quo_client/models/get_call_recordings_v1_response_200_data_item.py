import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.get_call_recordings_v1_response_200_data_item_status_type_0 import (
    GetCallRecordingsV1Response200DataItemStatusType0,
)

T = TypeVar("T", bound="GetCallRecordingsV1Response200DataItem")


@_attrs_define
class GetCallRecordingsV1Response200DataItem:
    """
    Attributes:
        duration (Union[None, int]):
        id (str): The unique identifier of the call recording.
        start_time (Union[None, datetime.datetime]):
        status (Union[GetCallRecordingsV1Response200DataItemStatusType0, None]):
        type_ (Union[None, str]):
        url (Union[None, str]):
    """

    duration: Union[None, int]
    id: str
    start_time: Union[None, datetime.datetime]
    status: Union[GetCallRecordingsV1Response200DataItemStatusType0, None]
    type_: Union[None, str]
    url: Union[None, str]

    def to_dict(self) -> dict[str, Any]:
        duration: Union[None, int]
        duration = self.duration

        id = self.id

        start_time: Union[None, str]
        if isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        status: Union[None, str]
        if isinstance(self.status, GetCallRecordingsV1Response200DataItemStatusType0):
            status = self.status.value
        else:
            status = self.status

        type_: Union[None, str]
        type_ = self.type_

        url: Union[None, str]
        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration": duration,
                "id": id,
                "startTime": start_time,
                "status": status,
                "type": type_,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_duration(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        duration = _parse_duration(d.pop("duration"))

        id = d.pop("id")

        def _parse_start_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        start_time = _parse_start_time(d.pop("startTime"))

        def _parse_status(data: object) -> Union[GetCallRecordingsV1Response200DataItemStatusType0, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = GetCallRecordingsV1Response200DataItemStatusType0(data)

                return status_type_0
            except:  # noqa: E722
                pass
            return cast(Union[GetCallRecordingsV1Response200DataItemStatusType0, None], data)

        status = _parse_status(d.pop("status"))

        def _parse_type_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        url = _parse_url(d.pop("url"))

        get_call_recordings_v1_response_200_data_item = cls(
            duration=duration,
            id=id,
            start_time=start_time,
            status=status,
            type_=type_,
            url=url,
        )

        return get_call_recordings_v1_response_200_data_item
