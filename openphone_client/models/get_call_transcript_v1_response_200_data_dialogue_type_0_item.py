from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCallTranscriptV1Response200DataDialogueType0Item")


@_attrs_define
class GetCallTranscriptV1Response200DataDialogueType0Item:
    """
    Attributes:
        content (str): The transcribed text of a specific dialogue segment.
        start (float): The start time of the dialogue segment in seconds, relative to the beginning of the call.
        end (float): The end time of the dialogue segment in seconds, relative to the beginning of the call.
        identifier (str): The phone number of the participant who spoke during this dialogue segment.
        user_id (Union[None, str]):
    """

    content: str
    start: float
    end: float
    identifier: str
    user_id: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        start = self.start

        end = self.end

        identifier = self.identifier

        user_id: Union[None, str]
        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "start": start,
                "end": end,
                "identifier": identifier,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        start = d.pop("start")

        end = d.pop("end")

        identifier = d.pop("identifier")

        def _parse_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_id = _parse_user_id(d.pop("userId"))

        get_call_transcript_v1_response_200_data_dialogue_type_0_item = cls(
            content=content,
            start=start,
            end=end,
            identifier=identifier,
            user_id=user_id,
        )

        get_call_transcript_v1_response_200_data_dialogue_type_0_item.additional_properties = d
        return get_call_transcript_v1_response_200_data_dialogue_type_0_item

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
