from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_gemaps_extract_response_200_chunk_info import (
        GetGemapsExtractResponse200ChunkInfo,
    )
    from ..models.get_gemaps_extract_response_200_combined_features import (
        GetGemapsExtractResponse200CombinedFeatures,
    )
    from ..models.get_gemaps_extract_response_200_features import (
        GetGemapsExtractResponse200Features,
    )
    from ..models.get_gemaps_extract_response_200_metadata import (
        GetGemapsExtractResponse200Metadata,
    )


T = TypeVar("T", bound="GetGemapsExtractResponse200")


@_attrs_define
class GetGemapsExtractResponse200:
    """
    Attributes:
        features (GetGemapsExtractResponse200Features | Unset): Object (files up to 8 s) of GeMAPS v01b functionals as
            emitted by openSMILE (e.g. F0semitoneFrom27.5Hz_sma3nz_amean, loudness_sma3_amean, jitterLocal_sma3nz_amean,
            shimmerLocaldB_sma3nz_amean, HNRdBACF_sma3nz_amean, F1frequency_sma3nz_amean), plus speech_percentage and
            silence_percentage. feature_count gives the number of keys. Refer to the openSMILE GeMAPSv01b configuration for
            the canonical list.
        combined_features (GetGemapsExtractResponse200CombinedFeatures | Unset): Object (files over 8 s) with one entry
            per feature: `{ mean, min, max, std, median, count }` across chunks; the per-chunk results are in `chunks`.
        chunk_info (GetGemapsExtractResponse200ChunkInfo | Unset): Object describing chunking: `{ total_chunks: number,
            current_chunk: number, start_time: number, duration: number, is_chunked: boolean }`. For files ≤ 8 s, is_chunked
            is false and the whole file produces one result.
        metadata (GetGemapsExtractResponse200Metadata | Unset): Object: `{ file_id: string, processing_duration_seconds:
            number, analysis_type: "single_chunk" | "chunked" }`.
    """

    features: GetGemapsExtractResponse200Features | Unset = UNSET
    combined_features: GetGemapsExtractResponse200CombinedFeatures | Unset = UNSET
    chunk_info: GetGemapsExtractResponse200ChunkInfo | Unset = UNSET
    metadata: GetGemapsExtractResponse200Metadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        combined_features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.combined_features, Unset):
            combined_features = self.combined_features.to_dict()

        chunk_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chunk_info, Unset):
            chunk_info = self.chunk_info.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if features is not UNSET:
            field_dict["features"] = features
        if combined_features is not UNSET:
            field_dict["combined_features"] = combined_features
        if chunk_info is not UNSET:
            field_dict["chunk_info"] = chunk_info
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_gemaps_extract_response_200_chunk_info import (
            GetGemapsExtractResponse200ChunkInfo,
        )
        from ..models.get_gemaps_extract_response_200_combined_features import (
            GetGemapsExtractResponse200CombinedFeatures,
        )
        from ..models.get_gemaps_extract_response_200_features import (
            GetGemapsExtractResponse200Features,
        )
        from ..models.get_gemaps_extract_response_200_metadata import (
            GetGemapsExtractResponse200Metadata,
        )

        d = dict(src_dict)
        _features = d.pop("features", UNSET)
        features: GetGemapsExtractResponse200Features | Unset
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = GetGemapsExtractResponse200Features.from_dict(_features)

        _combined_features = d.pop("combined_features", UNSET)
        combined_features: GetGemapsExtractResponse200CombinedFeatures | Unset
        if isinstance(_combined_features, Unset):
            combined_features = UNSET
        else:
            combined_features = GetGemapsExtractResponse200CombinedFeatures.from_dict(
                _combined_features
            )

        _chunk_info = d.pop("chunk_info", UNSET)
        chunk_info: GetGemapsExtractResponse200ChunkInfo | Unset
        if isinstance(_chunk_info, Unset):
            chunk_info = UNSET
        else:
            chunk_info = GetGemapsExtractResponse200ChunkInfo.from_dict(_chunk_info)

        _metadata = d.pop("metadata", UNSET)
        metadata: GetGemapsExtractResponse200Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GetGemapsExtractResponse200Metadata.from_dict(_metadata)

        get_gemaps_extract_response_200 = cls(
            features=features,
            combined_features=combined_features,
            chunk_info=chunk_info,
            metadata=metadata,
        )

        get_gemaps_extract_response_200.additional_properties = d
        return get_gemaps_extract_response_200

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
