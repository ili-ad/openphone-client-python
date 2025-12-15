from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_call_summary_v1_response_200_data_status import GetCallSummaryV1Response200DataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_call_summary_v1_response_200_data_jobs_type_0_item import (
        GetCallSummaryV1Response200DataJobsType0Item,
    )


T = TypeVar("T", bound="GetCallSummaryV1Response200Data")


@_attrs_define
class GetCallSummaryV1Response200Data:
    """
    Attributes:
        call_id (str): The unique identifier of the call to which this summary belongs.
        next_steps (Union[None, list[str]]):
        status (GetCallSummaryV1Response200DataStatus): The status of the call summary.
        summary (Union[None, list[str]]):
        jobs (Union[None, Unset, list['GetCallSummaryV1Response200DataJobsType0Item']]):
    """

    call_id: str
    next_steps: Union[None, list[str]]
    status: GetCallSummaryV1Response200DataStatus
    summary: Union[None, list[str]]
    jobs: Union[None, Unset, list["GetCallSummaryV1Response200DataJobsType0Item"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        next_steps: Union[None, list[str]]
        if isinstance(self.next_steps, list):
            next_steps = self.next_steps

        else:
            next_steps = self.next_steps

        status = self.status.value

        summary: Union[None, list[str]]
        if isinstance(self.summary, list):
            summary = self.summary

        else:
            summary = self.summary

        jobs: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.jobs, Unset):
            jobs = UNSET
        elif isinstance(self.jobs, list):
            jobs = []
            for jobs_type_0_item_data in self.jobs:
                jobs_type_0_item = jobs_type_0_item_data.to_dict()
                jobs.append(jobs_type_0_item)

        else:
            jobs = self.jobs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "callId": call_id,
                "nextSteps": next_steps,
                "status": status,
                "summary": summary,
            }
        )
        if jobs is not UNSET:
            field_dict["jobs"] = jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_call_summary_v1_response_200_data_jobs_type_0_item import (
            GetCallSummaryV1Response200DataJobsType0Item,
        )

        d = dict(src_dict)
        call_id = d.pop("callId")

        def _parse_next_steps(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                next_steps_type_0 = cast(list[str], data)

                return next_steps_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        next_steps = _parse_next_steps(d.pop("nextSteps"))

        status = GetCallSummaryV1Response200DataStatus(d.pop("status"))

        def _parse_summary(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                summary_type_0 = cast(list[str], data)

                return summary_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        summary = _parse_summary(d.pop("summary"))

        def _parse_jobs(data: object) -> Union[None, Unset, list["GetCallSummaryV1Response200DataJobsType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                jobs_type_0 = []
                _jobs_type_0 = data
                for jobs_type_0_item_data in _jobs_type_0:
                    jobs_type_0_item = GetCallSummaryV1Response200DataJobsType0Item.from_dict(jobs_type_0_item_data)

                    jobs_type_0.append(jobs_type_0_item)

                return jobs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["GetCallSummaryV1Response200DataJobsType0Item"]], data)

        jobs = _parse_jobs(d.pop("jobs", UNSET))

        get_call_summary_v1_response_200_data = cls(
            call_id=call_id,
            next_steps=next_steps,
            status=status,
            summary=summary,
            jobs=jobs,
        )

        get_call_summary_v1_response_200_data.additional_properties = d
        return get_call_summary_v1_response_200_data

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
