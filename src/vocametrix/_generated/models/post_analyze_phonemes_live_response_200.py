from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_analyze_phonemes_live_response_200_phoneme_timings_item import (
        PostAnalyzePhonemesLiveResponse200PhonemeTimingsItem,
    )
    from ..models.post_analyze_phonemes_live_response_200_phonemes_item import (
        PostAnalyzePhonemesLiveResponse200PhonemesItem,
    )


T = TypeVar("T", bound="PostAnalyzePhonemesLiveResponse200")


@_attrs_define
class PostAnalyzePhonemesLiveResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean — true when analysis completed (including the empty-result "Silence detected"
            case).
        status (str | Unset): "completed" on success.
        message (str | Unset): Descriptive message, e.g. "Analysis completed successfully" or "Silence detected".
        language (str | Unset): Echoed language code processed.
        transcription (str | Unset): Space-separated sequence of detected phonemes (empty string if silence).
        phoneme_count (float | Unset): Total number of phonemes detected.
        phonemes (list[PostAnalyzePhonemesLiveResponse200PhonemesItem] | Unset): Array of the phoneme labels detected,
            in order.
        phoneme_timings (list[PostAnalyzePhonemesLiveResponse200PhonemeTimingsItem] | Unset): Array of `{ phoneme,
            start, end, duration, confidence, second_phoneme, second_confidence }` — one entry per phoneme.
            `second_phoneme`/`second_confidence` (French champion models only) is the runner-up at that phoneme's most
            confident frame, or null if unavailable.
        audio_info (str | Unset): `{ duration_seconds, sample_rate }` — sample_rate is always 16000.
    """

    success: bool | Unset = UNSET
    status: str | Unset = UNSET
    message: str | Unset = UNSET
    language: str | Unset = UNSET
    transcription: str | Unset = UNSET
    phoneme_count: float | Unset = UNSET
    phonemes: list[PostAnalyzePhonemesLiveResponse200PhonemesItem] | Unset = UNSET
    phoneme_timings: list[PostAnalyzePhonemesLiveResponse200PhonemeTimingsItem] | Unset = UNSET
    audio_info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        message = self.message

        language = self.language

        transcription = self.transcription

        phoneme_count = self.phoneme_count

        phonemes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phonemes, Unset):
            phonemes = []
            for phonemes_item_data in self.phonemes:
                phonemes_item = phonemes_item_data.to_dict()
                phonemes.append(phonemes_item)

        phoneme_timings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phoneme_timings, Unset):
            phoneme_timings = []
            for phoneme_timings_item_data in self.phoneme_timings:
                phoneme_timings_item = phoneme_timings_item_data.to_dict()
                phoneme_timings.append(phoneme_timings_item)

        audio_info = self.audio_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if language is not UNSET:
            field_dict["language"] = language
        if transcription is not UNSET:
            field_dict["transcription"] = transcription
        if phoneme_count is not UNSET:
            field_dict["phoneme_count"] = phoneme_count
        if phonemes is not UNSET:
            field_dict["phonemes"] = phonemes
        if phoneme_timings is not UNSET:
            field_dict["phoneme_timings"] = phoneme_timings
        if audio_info is not UNSET:
            field_dict["audio_info"] = audio_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_analyze_phonemes_live_response_200_phoneme_timings_item import (
            PostAnalyzePhonemesLiveResponse200PhonemeTimingsItem,
        )
        from ..models.post_analyze_phonemes_live_response_200_phonemes_item import (
            PostAnalyzePhonemesLiveResponse200PhonemesItem,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        language = d.pop("language", UNSET)

        transcription = d.pop("transcription", UNSET)

        phoneme_count = d.pop("phoneme_count", UNSET)

        _phonemes = d.pop("phonemes", UNSET)
        phonemes: list[PostAnalyzePhonemesLiveResponse200PhonemesItem] | Unset = UNSET
        if _phonemes is not UNSET:
            phonemes = []
            for phonemes_item_data in _phonemes:
                phonemes_item = PostAnalyzePhonemesLiveResponse200PhonemesItem.from_dict(
                    phonemes_item_data
                )

                phonemes.append(phonemes_item)

        _phoneme_timings = d.pop("phoneme_timings", UNSET)
        phoneme_timings: list[PostAnalyzePhonemesLiveResponse200PhonemeTimingsItem] | Unset = UNSET
        if _phoneme_timings is not UNSET:
            phoneme_timings = []
            for phoneme_timings_item_data in _phoneme_timings:
                phoneme_timings_item = (
                    PostAnalyzePhonemesLiveResponse200PhonemeTimingsItem.from_dict(
                        phoneme_timings_item_data
                    )
                )

                phoneme_timings.append(phoneme_timings_item)

        audio_info = d.pop("audio_info", UNSET)

        post_analyze_phonemes_live_response_200 = cls(
            success=success,
            status=status,
            message=message,
            language=language,
            transcription=transcription,
            phoneme_count=phoneme_count,
            phonemes=phonemes,
            phoneme_timings=phoneme_timings,
            audio_info=audio_info,
        )

        post_analyze_phonemes_live_response_200.additional_properties = d
        return post_analyze_phonemes_live_response_200

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
