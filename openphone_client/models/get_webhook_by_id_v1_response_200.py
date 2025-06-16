from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_webhook_by_id_v1_response_200_data_type_0 import GetWebhookByIdV1Response200DataType0
    from ..models.get_webhook_by_id_v1_response_200_data_type_1 import GetWebhookByIdV1Response200DataType1
    from ..models.get_webhook_by_id_v1_response_200_data_type_2 import GetWebhookByIdV1Response200DataType2
    from ..models.get_webhook_by_id_v1_response_200_data_type_3 import GetWebhookByIdV1Response200DataType3


T = TypeVar("T", bound="GetWebhookByIdV1Response200")


@_attrs_define
class GetWebhookByIdV1Response200:
    """
    Attributes:
        data (Union['GetWebhookByIdV1Response200DataType0', 'GetWebhookByIdV1Response200DataType1',
            'GetWebhookByIdV1Response200DataType2', 'GetWebhookByIdV1Response200DataType3']):
    """

    data: Union[
        "GetWebhookByIdV1Response200DataType0",
        "GetWebhookByIdV1Response200DataType1",
        "GetWebhookByIdV1Response200DataType2",
        "GetWebhookByIdV1Response200DataType3",
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_webhook_by_id_v1_response_200_data_type_0 import GetWebhookByIdV1Response200DataType0
        from ..models.get_webhook_by_id_v1_response_200_data_type_1 import GetWebhookByIdV1Response200DataType1
        from ..models.get_webhook_by_id_v1_response_200_data_type_2 import GetWebhookByIdV1Response200DataType2

        data: dict[str, Any]
        if isinstance(self.data, GetWebhookByIdV1Response200DataType0):
            data = self.data.to_dict()
        elif isinstance(self.data, GetWebhookByIdV1Response200DataType1):
            data = self.data.to_dict()
        elif isinstance(self.data, GetWebhookByIdV1Response200DataType2):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

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
        from ..models.get_webhook_by_id_v1_response_200_data_type_0 import GetWebhookByIdV1Response200DataType0
        from ..models.get_webhook_by_id_v1_response_200_data_type_1 import GetWebhookByIdV1Response200DataType1
        from ..models.get_webhook_by_id_v1_response_200_data_type_2 import GetWebhookByIdV1Response200DataType2
        from ..models.get_webhook_by_id_v1_response_200_data_type_3 import GetWebhookByIdV1Response200DataType3

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> Union[
            "GetWebhookByIdV1Response200DataType0",
            "GetWebhookByIdV1Response200DataType1",
            "GetWebhookByIdV1Response200DataType2",
            "GetWebhookByIdV1Response200DataType3",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = GetWebhookByIdV1Response200DataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = GetWebhookByIdV1Response200DataType1.from_dict(data)

                return data_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_2 = GetWebhookByIdV1Response200DataType2.from_dict(data)

                return data_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_3 = GetWebhookByIdV1Response200DataType3.from_dict(data)

            return data_type_3

        data = _parse_data(d.pop("data"))

        get_webhook_by_id_v1_response_200 = cls(
            data=data,
        )

        get_webhook_by_id_v1_response_200.additional_properties = d
        return get_webhook_by_id_v1_response_200

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
