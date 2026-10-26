from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_measure_ddk_response_200_norm import GetMeasureDdkResponse200Norm
    from ..models.get_measure_ddk_response_200_onsets_s_item import (
        GetMeasureDdkResponse200OnsetsSItem,
    )


T = TypeVar("T", bound="GetMeasureDdkResponse200")


@_attrs_define
class GetMeasureDdkResponse200:
    """
    Attributes:
        task (str | Unset): Echo of the task parameter. Example: "pataka"
        syllables (float | Unset): number - Syllables detected. Example: 36
        rate_first9 (float | Unset): number - Syllables per second from the onset of syllable 1 to the onset of syllable
            10 (the window of the norms); absent below 10 syllables. Example: 7.32
        rate_overall (float | Unset): number - Syllables per second over the whole repetition. Example: 7.43
        cov_percent (float | Unset): number - Coefficient of variation of the intervals between syllable onsets, in %;
            higher means less regular. Example: 13.6
        npvi (float | Unset): number - Normalized pairwise variability index of the intervals; higher means less
            regular. Example: 18.6
        interval_slope_ms (float | Unset): number - Change of the interval length per syllable, in ms; negative means
            the speaker accelerates. Example: -0.09
        norm (GetMeasureDdkResponse200Norm | Unset): object - {source, mean, sd, min, max, z}: the Pierce et al. 2013
            norm (syllables per second) for this gender and age group, and the z-score of rate_first9; null without gender
            and age, outside 65-86, or for pa_steady.
        onsets_s (list[GetMeasureDdkResponse200OnsetsSItem] | Unset): array - Onset time of each syllable, in seconds.
    """

    task: str | Unset = UNSET
    syllables: float | Unset = UNSET
    rate_first9: float | Unset = UNSET
    rate_overall: float | Unset = UNSET
    cov_percent: float | Unset = UNSET
    npvi: float | Unset = UNSET
    interval_slope_ms: float | Unset = UNSET
    norm: GetMeasureDdkResponse200Norm | Unset = UNSET
    onsets_s: list[GetMeasureDdkResponse200OnsetsSItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        syllables = self.syllables

        rate_first9 = self.rate_first9

        rate_overall = self.rate_overall

        cov_percent = self.cov_percent

        npvi = self.npvi

        interval_slope_ms = self.interval_slope_ms

        norm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.norm, Unset):
            norm = self.norm.to_dict()

        onsets_s: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.onsets_s, Unset):
            onsets_s = []
            for onsets_s_item_data in self.onsets_s:
                onsets_s_item = onsets_s_item_data.to_dict()
                onsets_s.append(onsets_s_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task is not UNSET:
            field_dict["task"] = task
        if syllables is not UNSET:
            field_dict["syllables"] = syllables
        if rate_first9 is not UNSET:
            field_dict["rate_first9"] = rate_first9
        if rate_overall is not UNSET:
            field_dict["rate_overall"] = rate_overall
        if cov_percent is not UNSET:
            field_dict["cov_percent"] = cov_percent
        if npvi is not UNSET:
            field_dict["npvi"] = npvi
        if interval_slope_ms is not UNSET:
            field_dict["interval_slope_ms"] = interval_slope_ms
        if norm is not UNSET:
            field_dict["norm"] = norm
        if onsets_s is not UNSET:
            field_dict["onsets_s"] = onsets_s

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_measure_ddk_response_200_norm import GetMeasureDdkResponse200Norm
        from ..models.get_measure_ddk_response_200_onsets_s_item import (
            GetMeasureDdkResponse200OnsetsSItem,
        )

        d = dict(src_dict)
        task = d.pop("task", UNSET)

        syllables = d.pop("syllables", UNSET)

        rate_first9 = d.pop("rate_first9", UNSET)

        rate_overall = d.pop("rate_overall", UNSET)

        cov_percent = d.pop("cov_percent", UNSET)

        npvi = d.pop("npvi", UNSET)

        interval_slope_ms = d.pop("interval_slope_ms", UNSET)

        _norm = d.pop("norm", UNSET)
        norm: GetMeasureDdkResponse200Norm | Unset
        if isinstance(_norm, Unset):
            norm = UNSET
        else:
            norm = GetMeasureDdkResponse200Norm.from_dict(_norm)

        _onsets_s = d.pop("onsets_s", UNSET)
        onsets_s: list[GetMeasureDdkResponse200OnsetsSItem] | Unset = UNSET
        if _onsets_s is not UNSET:
            onsets_s = []
            for onsets_s_item_data in _onsets_s:
                onsets_s_item = GetMeasureDdkResponse200OnsetsSItem.from_dict(onsets_s_item_data)

                onsets_s.append(onsets_s_item)

        get_measure_ddk_response_200 = cls(
            task=task,
            syllables=syllables,
            rate_first9=rate_first9,
            rate_overall=rate_overall,
            cov_percent=cov_percent,
            npvi=npvi,
            interval_slope_ms=interval_slope_ms,
            norm=norm,
            onsets_s=onsets_s,
        )

        get_measure_ddk_response_200.additional_properties = d
        return get_measure_ddk_response_200

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
