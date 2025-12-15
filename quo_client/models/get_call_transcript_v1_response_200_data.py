import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_call_transcript_v1_response_200_data_status import GetCallTranscriptV1Response200DataStatus

if TYPE_CHECKING:
    from ..models.get_call_transcript_v1_response_200_data_dialogue_type_0_item import (
        GetCallTranscriptV1Response200DataDialogueType0Item,
    )


T = TypeVar("T", bound="GetCallTranscriptV1Response200Data")


@_attrs_define
class GetCallTranscriptV1Response200Data:
    """
    Attributes:
        call_id (str): The unique identifier of the call to which this transcript belongs.
        created_at (datetime.datetime): The timestamp when the transcription was created, in ISO 8601 format.
        dialogue (Union[None, list['GetCallTranscriptV1Response200DataDialogueType0Item']]):
        duration (float): The total duration of the transcribed call in seconds.
        status (GetCallTranscriptV1Response200DataStatus): The status of the call transcription.
    """

    call_id: str
    created_at: datetime.datetime
    dialogue: Union[None, list["GetCallTranscriptV1Response200DataDialogueType0Item"]]
    duration: float
    status: GetCallTranscriptV1Response200DataStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        created_at = self.created_at.isoformat()

        dialogue: Union[None, list[dict[str, Any]]]
        if isinstance(self.dialogue, list):
            dialogue = []
            for dialogue_type_0_item_data in self.dialogue:
                dialogue_type_0_item = dialogue_type_0_item_data.to_dict()
                dialogue.append(dialogue_type_0_item)

        else:
            dialogue = self.dialogue

        duration = self.duration

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "callId": call_id,
                "createdAt": created_at,
                "dialogue": dialogue,
                "duration": duration,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_call_transcript_v1_response_200_data_dialogue_type_0_item import (
            GetCallTranscriptV1Response200DataDialogueType0Item,
        )

        d = dict(src_dict)
        call_id = d.pop("callId")

        created_at = isoparse(d.pop("createdAt"))

        def _parse_dialogue(data: object) -> Union[None, list["GetCallTranscriptV1Response200DataDialogueType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dialogue_type_0 = []
                _dialogue_type_0 = data
                for dialogue_type_0_item_data in _dialogue_type_0:
                    dialogue_type_0_item = GetCallTranscriptV1Response200DataDialogueType0Item.from_dict(
                        dialogue_type_0_item_data
                    )

                    dialogue_type_0.append(dialogue_type_0_item)

                return dialogue_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["GetCallTranscriptV1Response200DataDialogueType0Item"]], data)

        dialogue = _parse_dialogue(d.pop("dialogue"))

        duration = d.pop("duration")

        status = GetCallTranscriptV1Response200DataStatus(d.pop("status"))

        get_call_transcript_v1_response_200_data = cls(
            call_id=call_id,
            created_at=created_at,
            dialogue=dialogue,
            duration=duration,
            status=status,
        )

        get_call_transcript_v1_response_200_data.additional_properties = d
        return get_call_transcript_v1_response_200_data

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
