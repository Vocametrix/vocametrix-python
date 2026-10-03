from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostVoiceAssessmentResponse200Summary")


@_attrs_define
class PostVoiceAssessmentResponse200Summary:
    """object - Key results: avqi, avqi_cpps, jitter_local_percent, shimmer_local_percent, mean_f0_hz, hnr_db, cpp_db, gne,
    h1_h2_db, abi, the severities (jitter, shimmer, hnr, cpp, breathiness) and abnormal_flags [{measure, severity}]. A
    key is absent when its measure failed.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_voice_assessment_response_200_summary = cls()

        post_voice_assessment_response_200_summary.additional_properties = d
        return post_voice_assessment_response_200_summary

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
