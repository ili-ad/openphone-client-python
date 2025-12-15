import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.list_webhooks_v1_response_200_data_item_type_1_events_item import (
    ListWebhooksV1Response200DataItemType1EventsItem,
)
from ..models.list_webhooks_v1_response_200_data_item_type_1_status import ListWebhooksV1Response200DataItemType1Status

T = TypeVar("T", bound="ListWebhooksV1Response200DataItemType1")


@_attrs_define
class ListWebhooksV1Response200DataItemType1:
    """
    Attributes:
        id (str): The webhook's ID
        user_id (str): The unique identifier of the user that created the webhook.
        org_id (str): The unique identifier of the organization the webhook belongs to
        label (Union[None, str]):
        status (ListWebhooksV1Response200DataItemType1Status): The status of the webhook. Default:
            ListWebhooksV1Response200DataItemType1Status.ENABLED.
        url (str): The endpoint that receives events from the webhook.
        key (str): Webhook key
        created_at (datetime.datetime): The date the webhook was created at, in ISO_8601 format.
        updated_at (datetime.datetime): The date the webhook was created at, in ISO_8601 format.
        deleted_at (Union[None, datetime.datetime]):
        events (list[ListWebhooksV1Response200DataItemType1EventsItem]):
        resource_ids (Union[list[Literal['*']], list[str]]):
    """

    id: str
    user_id: str
    org_id: str
    label: Union[None, str]
    url: str
    key: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Union[None, datetime.datetime]
    events: list[ListWebhooksV1Response200DataItemType1EventsItem]
    resource_ids: Union[list[Literal["*"]], list[str]]
    status: ListWebhooksV1Response200DataItemType1Status = ListWebhooksV1Response200DataItemType1Status.ENABLED
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        org_id = self.org_id

        label: Union[None, str]
        label = self.label

        status = self.status.value

        url = self.url

        key = self.key

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: Union[None, str]
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        resource_ids: Union[list[Literal["*"]], list[str]]
        if isinstance(self.resource_ids, list):
            resource_ids = self.resource_ids

        else:
            resource_ids = self.resource_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "orgId": org_id,
                "label": label,
                "status": status,
                "url": url,
                "key": key,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "deletedAt": deleted_at,
                "events": events,
                "resourceIds": resource_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        org_id = d.pop("orgId")

        def _parse_label(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        label = _parse_label(d.pop("label"))

        status = ListWebhooksV1Response200DataItemType1Status(d.pop("status"))

        url = d.pop("url")

        key = d.pop("key")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

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

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = ListWebhooksV1Response200DataItemType1EventsItem(events_item_data)

            events.append(events_item)

        def _parse_resource_ids(data: object) -> Union[list[Literal["*"]], list[str]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_ids_type_0 = cast(list[str], data)

                return resource_ids_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            resource_ids_type_1 = []
            _resource_ids_type_1 = data
            for resource_ids_type_1_item_data in _resource_ids_type_1:
                resource_ids_type_1_item = cast(Literal["*"], resource_ids_type_1_item_data)
                if resource_ids_type_1_item != "*":
                    raise ValueError(f"resourceIds_type_1_item must match const '*', got '{resource_ids_type_1_item}'")
                resource_ids_type_1.append(resource_ids_type_1_item)

            return resource_ids_type_1

        resource_ids = _parse_resource_ids(d.pop("resourceIds"))

        list_webhooks_v1_response_200_data_item_type_1 = cls(
            id=id,
            user_id=user_id,
            org_id=org_id,
            label=label,
            status=status,
            url=url,
            key=key,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            events=events,
            resource_ids=resource_ids,
        )

        list_webhooks_v1_response_200_data_item_type_1.additional_properties = d
        return list_webhooks_v1_response_200_data_item_type_1

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
