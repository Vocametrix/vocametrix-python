from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostEstimateFormantsBody")


@_attrs_define
class PostEstimateFormantsBody:
    """
    Attributes:
        file_id (str): ID returned by /api/assignFileId - REQUIRED
        start_sec (float): Start of the segment in seconds; 0 with stop_sec 0 analyses the whole file - REQUIRED
        stop_sec (float): End of the segment in seconds; 0 with start_sec 0 analyses the whole file - REQUIRED
        language (str | Unset): Language code, e.g. "fr-FR". Optional, default "en-US"
        gender (str | Unset): "male" or "female". Optional, default "female"
        age_group (str | Unset): "adult" or "child". Optional, default "adult"
        sustained_vowel (bool | Unset): true for a sustained vowel: the most stable window is analysed. Optional,
            default false
    """

    file_id: str
    start_sec: float
    stop_sec: float
    language: str | Unset = UNSET
    gender: str | Unset = UNSET
    age_group: str | Unset = UNSET
    sustained_vowel: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        start_sec = self.start_sec

        stop_sec = self.stop_sec

        language = self.language

        gender = self.gender

        age_group = self.age_group

        sustained_vowel = self.sustained_vowel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileId": file_id,
                "start_sec": start_sec,
                "stop_sec": stop_sec,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if gender is not UNSET:
            field_dict["gender"] = gender
        if age_group is not UNSET:
            field_dict["ageGroup"] = age_group
        if sustained_vowel is not UNSET:
            field_dict["sustained_vowel"] = sustained_vowel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("fileId")

        start_sec = d.pop("start_sec")

        stop_sec = d.pop("stop_sec")

        language = d.pop("language", UNSET)

        gender = d.pop("gender", UNSET)

        age_group = d.pop("ageGroup", UNSET)

        sustained_vowel = d.pop("sustained_vowel", UNSET)

        post_estimate_formants_body = cls(
            file_id=file_id,
            start_sec=start_sec,
            stop_sec=stop_sec,
            language=language,
            gender=gender,
            age_group=age_group,
            sustained_vowel=sustained_vowel,
        )

        post_estimate_formants_body.additional_properties = d
        return post_estimate_formants_body

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
