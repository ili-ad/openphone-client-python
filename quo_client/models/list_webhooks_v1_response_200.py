from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_webhooks_v1_response_200_data_item_type_0 import ListWebhooksV1Response200DataItemType0
    from ..models.list_webhooks_v1_response_200_data_item_type_1 import ListWebhooksV1Response200DataItemType1
    from ..models.list_webhooks_v1_response_200_data_item_type_2 import ListWebhooksV1Response200DataItemType2
    from ..models.list_webhooks_v1_response_200_data_item_type_3 import ListWebhooksV1Response200DataItemType3


T = TypeVar("T", bound="ListWebhooksV1Response200")


@_attrs_define
class ListWebhooksV1Response200:
    """
    Attributes:
        data (list[Union['ListWebhooksV1Response200DataItemType0', 'ListWebhooksV1Response200DataItemType1',
            'ListWebhooksV1Response200DataItemType2', 'ListWebhooksV1Response200DataItemType3']]):
    """

    data: list[
        Union[
            "ListWebhooksV1Response200DataItemType0",
            "ListWebhooksV1Response200DataItemType1",
            "ListWebhooksV1Response200DataItemType2",
            "ListWebhooksV1Response200DataItemType3",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_webhooks_v1_response_200_data_item_type_0 import ListWebhooksV1Response200DataItemType0
        from ..models.list_webhooks_v1_response_200_data_item_type_1 import ListWebhooksV1Response200DataItemType1
        from ..models.list_webhooks_v1_response_200_data_item_type_2 import ListWebhooksV1Response200DataItemType2

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, ListWebhooksV1Response200DataItemType0):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, ListWebhooksV1Response200DataItemType1):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, ListWebhooksV1Response200DataItemType2):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_webhooks_v1_response_200_data_item_type_0 import ListWebhooksV1Response200DataItemType0
        from ..models.list_webhooks_v1_response_200_data_item_type_1 import ListWebhooksV1Response200DataItemType1
        from ..models.list_webhooks_v1_response_200_data_item_type_2 import ListWebhooksV1Response200DataItemType2
        from ..models.list_webhooks_v1_response_200_data_item_type_3 import ListWebhooksV1Response200DataItemType3

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(
                data: object,
            ) -> Union[
                "ListWebhooksV1Response200DataItemType0",
                "ListWebhooksV1Response200DataItemType1",
                "ListWebhooksV1Response200DataItemType2",
                "ListWebhooksV1Response200DataItemType3",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = ListWebhooksV1Response200DataItemType0.from_dict(data)

                    return data_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = ListWebhooksV1Response200DataItemType1.from_dict(data)

                    return data_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_2 = ListWebhooksV1Response200DataItemType2.from_dict(data)

                    return data_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_3 = ListWebhooksV1Response200DataItemType3.from_dict(data)

                return data_item_type_3

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        list_webhooks_v1_response_200 = cls(
            data=data,
        )

        list_webhooks_v1_response_200.additional_properties = d
        return list_webhooks_v1_response_200

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
