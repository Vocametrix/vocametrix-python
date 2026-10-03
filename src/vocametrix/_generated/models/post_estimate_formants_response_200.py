from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_estimate_formants_response_200_formants import (
        PostEstimateFormantsResponse200Formants,
    )
    from ..models.post_estimate_formants_response_200_ipa_coordinates import (
        PostEstimateFormantsResponse200IpaCoordinates,
    )
    from ..models.post_estimate_formants_response_200_speaker_info import (
        PostEstimateFormantsResponse200SpeakerInfo,
    )
    from ..models.post_estimate_formants_response_200_suggestions_item import (
        PostEstimateFormantsResponse200SuggestionsItem,
    )


T = TypeVar("T", bound="PostEstimateFormantsResponse200")


@_attrs_define
class PostEstimateFormantsResponse200:
    """
    Attributes:
        success (bool | Unset): boolean - true when formants were measured
        formants (PostEstimateFormantsResponse200Formants | Unset): object - {f1_mean, f2_mean, f3_mean (Hz, f3 may be
            null), f1_std, f2_std, f3_std, num_measurements, f1_cv, f2_cv, estimated_f0}
        ipa_coordinates (PostEstimateFormantsResponse200IpaCoordinates | Unset): object - {x, y} between 0 and 1: x
            front to back, y close to open
        stability_score (float | Unset): number - Stability of the formant track
        language (str | Unset): Echo of the language parameter
        analysis_duration (float | Unset): number - Analysed duration in seconds
        speaker_info (PostEstimateFormantsResponse200SpeakerInfo | Unset): object - {gender, age_group} used for the
            analysis
        analysis_parameters (str | Unset): Parameter set used: "adult_female_default", "adult_male", "adult_female" or
            "child"
        error_type (str | Unset): When success is false: "insufficient_data", "analysis_failure", "f0_failure" or
            "unknown"
        suggestions (list[PostEstimateFormantsResponse200SuggestionsItem] | Unset): array - When success is false: tips
            to get a usable recording
    """

    success: bool | Unset = UNSET
    formants: PostEstimateFormantsResponse200Formants | Unset = UNSET
    ipa_coordinates: PostEstimateFormantsResponse200IpaCoordinates | Unset = UNSET
    stability_score: float | Unset = UNSET
    language: str | Unset = UNSET
    analysis_duration: float | Unset = UNSET
    speaker_info: PostEstimateFormantsResponse200SpeakerInfo | Unset = UNSET
    analysis_parameters: str | Unset = UNSET
    error_type: str | Unset = UNSET
    suggestions: list[PostEstimateFormantsResponse200SuggestionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        formants: dict[str, Any] | Unset = UNSET
        if not isinstance(self.formants, Unset):
            formants = self.formants.to_dict()

        ipa_coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipa_coordinates, Unset):
            ipa_coordinates = self.ipa_coordinates.to_dict()

        stability_score = self.stability_score

        language = self.language

        analysis_duration = self.analysis_duration

        speaker_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.speaker_info, Unset):
            speaker_info = self.speaker_info.to_dict()

        analysis_parameters = self.analysis_parameters

        error_type = self.error_type

        suggestions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()
                suggestions.append(suggestions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if formants is not UNSET:
            field_dict["formants"] = formants
        if ipa_coordinates is not UNSET:
            field_dict["ipa_coordinates"] = ipa_coordinates
        if stability_score is not UNSET:
            field_dict["stability_score"] = stability_score
        if language is not UNSET:
            field_dict["language"] = language
        if analysis_duration is not UNSET:
            field_dict["analysis_duration"] = analysis_duration
        if speaker_info is not UNSET:
            field_dict["speaker_info"] = speaker_info
        if analysis_parameters is not UNSET:
            field_dict["analysis_parameters"] = analysis_parameters
        if error_type is not UNSET:
            field_dict["error_type"] = error_type
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_estimate_formants_response_200_formants import (
            PostEstimateFormantsResponse200Formants,
        )
        from ..models.post_estimate_formants_response_200_ipa_coordinates import (
            PostEstimateFormantsResponse200IpaCoordinates,
        )
        from ..models.post_estimate_formants_response_200_speaker_info import (
            PostEstimateFormantsResponse200SpeakerInfo,
        )
        from ..models.post_estimate_formants_response_200_suggestions_item import (
            PostEstimateFormantsResponse200SuggestionsItem,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        _formants = d.pop("formants", UNSET)
        formants: PostEstimateFormantsResponse200Formants | Unset
        if isinstance(_formants, Unset):
            formants = UNSET
        else:
            formants = PostEstimateFormantsResponse200Formants.from_dict(_formants)

        _ipa_coordinates = d.pop("ipa_coordinates", UNSET)
        ipa_coordinates: PostEstimateFormantsResponse200IpaCoordinates | Unset
        if isinstance(_ipa_coordinates, Unset):
            ipa_coordinates = UNSET
        else:
            ipa_coordinates = PostEstimateFormantsResponse200IpaCoordinates.from_dict(
                _ipa_coordinates
            )

        stability_score = d.pop("stability_score", UNSET)

        language = d.pop("language", UNSET)

        analysis_duration = d.pop("analysis_duration", UNSET)

        _speaker_info = d.pop("speaker_info", UNSET)
        speaker_info: PostEstimateFormantsResponse200SpeakerInfo | Unset
        if isinstance(_speaker_info, Unset):
            speaker_info = UNSET
        else:
            speaker_info = PostEstimateFormantsResponse200SpeakerInfo.from_dict(_speaker_info)

        analysis_parameters = d.pop("analysis_parameters", UNSET)

        error_type = d.pop("error_type", UNSET)

        _suggestions = d.pop("suggestions", UNSET)
        suggestions: list[PostEstimateFormantsResponse200SuggestionsItem] | Unset = UNSET
        if _suggestions is not UNSET:
            suggestions = []
            for suggestions_item_data in _suggestions:
                suggestions_item = PostEstimateFormantsResponse200SuggestionsItem.from_dict(
                    suggestions_item_data
                )

                suggestions.append(suggestions_item)

        post_estimate_formants_response_200 = cls(
            success=success,
            formants=formants,
            ipa_coordinates=ipa_coordinates,
            stability_score=stability_score,
            language=language,
            analysis_duration=analysis_duration,
            speaker_info=speaker_info,
            analysis_parameters=analysis_parameters,
            error_type=error_type,
            suggestions=suggestions,
        )

        post_estimate_formants_response_200.additional_properties = d
        return post_estimate_formants_response_200

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
