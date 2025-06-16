from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_call_summary_webhook_v1_body_events_item import CreateCallSummaryWebhookV1BodyEventsItem
from ..models.create_call_summary_webhook_v1_body_status import CreateCallSummaryWebhookV1BodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCallSummaryWebhookV1Body")


@_attrs_define
class CreateCallSummaryWebhookV1Body:
    """
    Attributes:
        events (list[CreateCallSummaryWebhookV1BodyEventsItem]):
        url (str): The endpoint that receives events from the webhook.
        label (Union[Unset, str]): Webhook's label
        resource_ids (Union[Unset, list[Literal['*']], list[str]]):
        status (Union[Unset, CreateCallSummaryWebhookV1BodyStatus]): The status of the webhook. Default:
            CreateCallSummaryWebhookV1BodyStatus.ENABLED.
        user_id (Union[Unset, str]): The unique identifier of the user that creates the webhook. If not provided,
            default to workspace owner.
    """

    events: list[CreateCallSummaryWebhookV1BodyEventsItem]
    url: str
    label: Union[Unset, str] = UNSET
    resource_ids: Union[Unset, list[Literal["*"]], list[str]] = UNSET
    status: Union[Unset, CreateCallSummaryWebhookV1BodyStatus] = CreateCallSummaryWebhookV1BodyStatus.ENABLED
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        url = self.url

        label = self.label

        resource_ids: Union[Unset, list[Literal["*"]], list[str]]
        if isinstance(self.resource_ids, Unset):
            resource_ids = UNSET
        elif isinstance(self.resource_ids, list):
            resource_ids = self.resource_ids

        else:
            resource_ids = self.resource_ids

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "url": url,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if resource_ids is not UNSET:
            field_dict["resourceIds"] = resource_ids
        if status is not UNSET:
            field_dict["status"] = status
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = CreateCallSummaryWebhookV1BodyEventsItem(events_item_data)

            events.append(events_item)

        url = d.pop("url")

        label = d.pop("label", UNSET)

        def _parse_resource_ids(data: object) -> Union[Unset, list[Literal["*"]], list[str]]:
            if isinstance(data, Unset):
                return data
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

        resource_ids = _parse_resource_ids(d.pop("resourceIds", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateCallSummaryWebhookV1BodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateCallSummaryWebhookV1BodyStatus(_status)

        user_id = d.pop("userId", UNSET)

        create_call_summary_webhook_v1_body = cls(
            events=events,
            url=url,
            label=label,
            resource_ids=resource_ids,
            status=status,
            user_id=user_id,
        )

        create_call_summary_webhook_v1_body.additional_properties = d
        return create_call_summary_webhook_v1_body

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
