from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCallSummaryV1Response200DataJobsType0ItemResultDataItem")


@_attrs_define
class GetCallSummaryV1Response200DataJobsType0ItemResultDataItem:
    """
    Attributes:
        name (str):
        value (Union[bool, float, str]):
    """

    name: str
    value: Union[bool, float, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value: Union[bool, float, str]
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_value(data: object) -> Union[bool, float, str]:
            return cast(Union[bool, float, str], data)

        value = _parse_value(d.pop("value"))

        get_call_summary_v1_response_200_data_jobs_type_0_item_result_data_item = cls(
            name=name,
            value=value,
        )

        get_call_summary_v1_response_200_data_jobs_type_0_item_result_data_item.additional_properties = d
        return get_call_summary_v1_response_200_data_jobs_type_0_item_result_data_item

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
