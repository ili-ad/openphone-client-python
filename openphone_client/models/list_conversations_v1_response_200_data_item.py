import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ListConversationsV1Response200DataItem")


@_attrs_define
class ListConversationsV1Response200DataItem:
    """
    Attributes:
        assigned_to (Union[None, str]):
        created_at (Union[None, datetime.datetime]):
        deleted_at (Union[None, datetime.datetime]):
        id (str):
        last_activity_at (Union[None, datetime.datetime]):
        last_activity_id (Union[None, str]):
        muted_until (Union[None, datetime.datetime]):
        name (Union[None, str]):
        participants (list[str]):
        phone_number_id (str):
        snoozed_until (Union[None, datetime.datetime]):
        updated_at (Union[None, datetime.datetime]):
    """

    assigned_to: Union[None, str]
    created_at: Union[None, datetime.datetime]
    deleted_at: Union[None, datetime.datetime]
    id: str
    last_activity_at: Union[None, datetime.datetime]
    last_activity_id: Union[None, str]
    muted_until: Union[None, datetime.datetime]
    name: Union[None, str]
    participants: list[str]
    phone_number_id: str
    snoozed_until: Union[None, datetime.datetime]
    updated_at: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_to: Union[None, str]
        assigned_to = self.assigned_to

        created_at: Union[None, str]
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        deleted_at: Union[None, str]
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        id = self.id

        last_activity_at: Union[None, str]
        if isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        last_activity_id: Union[None, str]
        last_activity_id = self.last_activity_id

        muted_until: Union[None, str]
        if isinstance(self.muted_until, datetime.datetime):
            muted_until = self.muted_until.isoformat()
        else:
            muted_until = self.muted_until

        name: Union[None, str]
        name = self.name

        participants = self.participants

        phone_number_id = self.phone_number_id

        snoozed_until: Union[None, str]
        if isinstance(self.snoozed_until, datetime.datetime):
            snoozed_until = self.snoozed_until.isoformat()
        else:
            snoozed_until = self.snoozed_until

        updated_at: Union[None, str]
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignedTo": assigned_to,
                "createdAt": created_at,
                "deletedAt": deleted_at,
                "id": id,
                "lastActivityAt": last_activity_at,
                "lastActivityId": last_activity_id,
                "mutedUntil": muted_until,
                "name": name,
                "participants": participants,
                "phoneNumberId": phone_number_id,
                "snoozedUntil": snoozed_until,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assigned_to(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        assigned_to = _parse_assigned_to(d.pop("assignedTo"))

        def _parse_created_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("createdAt"))

        def _parse_deleted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))

        id = d.pop("id")

        def _parse_last_activity_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = isoparse(data)

                return last_activity_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt"))

        def _parse_last_activity_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_activity_id = _parse_last_activity_id(d.pop("lastActivityId"))

        def _parse_muted_until(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                muted_until_type_0 = isoparse(data)

                return muted_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        muted_until = _parse_muted_until(d.pop("mutedUntil"))

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        participants = cast(list[str], d.pop("participants"))

        phone_number_id = d.pop("phoneNumberId")

        def _parse_snoozed_until(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                snoozed_until_type_0 = isoparse(data)

                return snoozed_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        snoozed_until = _parse_snoozed_until(d.pop("snoozedUntil"))

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

        list_conversations_v1_response_200_data_item = cls(
            assigned_to=assigned_to,
            created_at=created_at,
            deleted_at=deleted_at,
            id=id,
            last_activity_at=last_activity_at,
            last_activity_id=last_activity_id,
            muted_until=muted_until,
            name=name,
            participants=participants,
            phone_number_id=phone_number_id,
            snoozed_until=snoozed_until,
            updated_at=updated_at,
        )

        list_conversations_v1_response_200_data_item.additional_properties = d
        return list_conversations_v1_response_200_data_item

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
