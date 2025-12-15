from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_call_webhook_v1_body_events_item import CreateCallWebhookV1BodyEventsItem
from ..models.create_call_webhook_v1_body_status import CreateCallWebhookV1BodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCallWebhookV1Body")


@_attrs_define
class CreateCallWebhookV1Body:
    """
    Attributes:
        url (str): The endpoint that receives events from the webhook.
        events (list[CreateCallWebhookV1BodyEventsItem]):
        resource_ids (Union[Unset, list[Literal['*']], list[str]]):
        user_id (Union[Unset, str]): The unique identifier of the user that creates the webhook. If not provided,
            default to workspace owner.
        label (Union[Unset, str]): Webhook's label
        status (Union[Unset, CreateCallWebhookV1BodyStatus]): The status of the webhook. Default:
            CreateCallWebhookV1BodyStatus.ENABLED.
    """

    url: str
    events: list[CreateCallWebhookV1BodyEventsItem]
    resource_ids: Union[Unset, list[Literal["*"]], list[str]] = UNSET
    user_id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    status: Union[Unset, CreateCallWebhookV1BodyStatus] = CreateCallWebhookV1BodyStatus.ENABLED
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        resource_ids: Union[Unset, list[Literal["*"]], list[str]]
        if isinstance(self.resource_ids, Unset):
            resource_ids = UNSET
        elif isinstance(self.resource_ids, list):
            resource_ids = self.resource_ids

        else:
            resource_ids = self.resource_ids

        user_id = self.user_id

        label = self.label

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "events": events,
            }
        )
        if resource_ids is not UNSET:
            field_dict["resourceIds"] = resource_ids
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if label is not UNSET:
            field_dict["label"] = label
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = CreateCallWebhookV1BodyEventsItem(events_item_data)

            events.append(events_item)

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

        user_id = d.pop("userId", UNSET)

        label = d.pop("label", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateCallWebhookV1BodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateCallWebhookV1BodyStatus(_status)

        create_call_webhook_v1_body = cls(
            url=url,
            events=events,
            resource_ids=resource_ids,
            user_id=user_id,
            label=label,
            status=status,
        )

        create_call_webhook_v1_body.additional_properties = d
        return create_call_webhook_v1_body

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
