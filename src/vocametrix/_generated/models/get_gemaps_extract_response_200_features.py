from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGemapsExtractResponse200Features")


@_attrs_define
class GetGemapsExtractResponse200Features:
    """Object (files up to 8 s) of GeMAPS v01b functionals as emitted by openSMILE (e.g. F0semitoneFrom27.5Hz_sma3nz_amean,
    loudness_sma3_amean, jitterLocal_sma3nz_amean, shimmerLocaldB_sma3nz_amean, HNRdBACF_sma3nz_amean,
    F1frequency_sma3nz_amean), plus speech_percentage and silence_percentage. feature_count gives the number of keys.
    Refer to the openSMILE GeMAPSv01b configuration for the canonical list.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_gemaps_extract_response_200_features = cls()

        get_gemaps_extract_response_200_features.additional_properties = d
        return get_gemaps_extract_response_200_features

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
