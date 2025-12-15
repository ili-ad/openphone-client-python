from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_call_summary_v1_response_200_data_jobs_type_0_item_result import (
        GetCallSummaryV1Response200DataJobsType0ItemResult,
    )


T = TypeVar("T", bound="GetCallSummaryV1Response200DataJobsType0Item")


@_attrs_define
class GetCallSummaryV1Response200DataJobsType0Item:
    """
    Attributes:
        icon (str):
        name (str):
        result (GetCallSummaryV1Response200DataJobsType0ItemResult):
    """

    icon: str
    name: str
    result: "GetCallSummaryV1Response200DataJobsType0ItemResult"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icon = self.icon

        name = self.name

        result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icon": icon,
                "name": name,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_call_summary_v1_response_200_data_jobs_type_0_item_result import (
            GetCallSummaryV1Response200DataJobsType0ItemResult,
        )

        d = dict(src_dict)
        icon = d.pop("icon")

        name = d.pop("name")

        result = GetCallSummaryV1Response200DataJobsType0ItemResult.from_dict(d.pop("result"))

        get_call_summary_v1_response_200_data_jobs_type_0_item = cls(
            icon=icon,
            name=name,
            result=result,
        )

        get_call_summary_v1_response_200_data_jobs_type_0_item.additional_properties = d
        return get_call_summary_v1_response_200_data_jobs_type_0_item

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
