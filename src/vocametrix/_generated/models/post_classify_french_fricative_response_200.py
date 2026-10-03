from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_classify_french_fricative_response_200_all_probabilities import (
        PostClassifyFrenchFricativeResponse200AllProbabilities,
    )


T = TypeVar("T", bound="PostClassifyFrenchFricativeResponse200")


@_attrs_define
class PostClassifyFrenchFricativeResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean — true if the classification succeeded.
        predicted_fricative (str | Unset): Predicted fricative (IPA).
        confidence (str | Unset): Confidence for the predicted fricative (0.0 - 1.0).
        all_probabilities (PostClassifyFrenchFricativeResponse200AllProbabilities | Unset): Object of probabilities for
            all 6 fricatives.
        audio_duration (float | Unset): Audio duration in seconds.
        processing_time_seconds (float | Unset): Server-side processing time in seconds.
        model_name (str | Unset): Model used, e.g. "fricative-aphasix-champion".
        expected_fricative_conditional (str | Unset): Echoed back only when expected_fricative/expectedFricative was
            provided in the request.
        is_correct_conditional (bool | Unset): Boolean — true when predicted_fricative matches expected_fricative.
        expected_fricative_probability_conditional (str | Unset): The model's probability for expected_fricative, from
            all_probabilities.
        score_conditional (int | Unset): expected_fricative_probability rounded to a 0-100 integer.
    """

    success: bool | Unset = UNSET
    predicted_fricative: str | Unset = UNSET
    confidence: str | Unset = UNSET
    all_probabilities: PostClassifyFrenchFricativeResponse200AllProbabilities | Unset = UNSET
    audio_duration: float | Unset = UNSET
    processing_time_seconds: float | Unset = UNSET
    model_name: str | Unset = UNSET
    expected_fricative_conditional: str | Unset = UNSET
    is_correct_conditional: bool | Unset = UNSET
    expected_fricative_probability_conditional: str | Unset = UNSET
    score_conditional: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        predicted_fricative = self.predicted_fricative

        confidence = self.confidence

        all_probabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_probabilities, Unset):
            all_probabilities = self.all_probabilities.to_dict()

        audio_duration = self.audio_duration

        processing_time_seconds = self.processing_time_seconds

        model_name = self.model_name

        expected_fricative_conditional = self.expected_fricative_conditional

        is_correct_conditional = self.is_correct_conditional

        expected_fricative_probability_conditional = self.expected_fricative_probability_conditional

        score_conditional = self.score_conditional

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if predicted_fricative is not UNSET:
            field_dict["predicted_fricative"] = predicted_fricative
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if all_probabilities is not UNSET:
            field_dict["all_probabilities"] = all_probabilities
        if audio_duration is not UNSET:
            field_dict["audio_duration"] = audio_duration
        if processing_time_seconds is not UNSET:
            field_dict["processing_time_seconds"] = processing_time_seconds
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if expected_fricative_conditional is not UNSET:
            field_dict["expected_fricative (conditional)"] = expected_fricative_conditional
        if is_correct_conditional is not UNSET:
            field_dict["is_correct (conditional)"] = is_correct_conditional
        if expected_fricative_probability_conditional is not UNSET:
            field_dict["expected_fricative_probability (conditional)"] = (
                expected_fricative_probability_conditional
            )
        if score_conditional is not UNSET:
            field_dict["score (conditional)"] = score_conditional

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_classify_french_fricative_response_200_all_probabilities import (
            PostClassifyFrenchFricativeResponse200AllProbabilities,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        predicted_fricative = d.pop("predicted_fricative", UNSET)

        confidence = d.pop("confidence", UNSET)

        _all_probabilities = d.pop("all_probabilities", UNSET)
        all_probabilities: PostClassifyFrenchFricativeResponse200AllProbabilities | Unset
        if isinstance(_all_probabilities, Unset):
            all_probabilities = UNSET
        else:
            all_probabilities = PostClassifyFrenchFricativeResponse200AllProbabilities.from_dict(
                _all_probabilities
            )

        audio_duration = d.pop("audio_duration", UNSET)

        processing_time_seconds = d.pop("processing_time_seconds", UNSET)

        model_name = d.pop("model_name", UNSET)

        expected_fricative_conditional = d.pop("expected_fricative (conditional)", UNSET)

        is_correct_conditional = d.pop("is_correct (conditional)", UNSET)

        expected_fricative_probability_conditional = d.pop(
            "expected_fricative_probability (conditional)", UNSET
        )

        score_conditional = d.pop("score (conditional)", UNSET)

        post_classify_french_fricative_response_200 = cls(
            success=success,
            predicted_fricative=predicted_fricative,
            confidence=confidence,
            all_probabilities=all_probabilities,
            audio_duration=audio_duration,
            processing_time_seconds=processing_time_seconds,
            model_name=model_name,
            expected_fricative_conditional=expected_fricative_conditional,
            is_correct_conditional=is_correct_conditional,
            expected_fricative_probability_conditional=expected_fricative_probability_conditional,
            score_conditional=score_conditional,
        )

        post_classify_french_fricative_response_200.additional_properties = d
        return post_classify_french_fricative_response_200

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
