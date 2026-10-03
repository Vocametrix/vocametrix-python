from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_voice_assessment_response_200_audio import (
        PostVoiceAssessmentResponse200Audio,
    )
    from ..models.post_voice_assessment_response_200_details import (
        PostVoiceAssessmentResponse200Details,
    )
    from ..models.post_voice_assessment_response_200_errors import (
        PostVoiceAssessmentResponse200Errors,
    )
    from ..models.post_voice_assessment_response_200_summary import (
        PostVoiceAssessmentResponse200Summary,
    )
    from ..models.post_voice_assessment_response_200_warnings_item import (
        PostVoiceAssessmentResponse200WarningsItem,
    )


T = TypeVar("T", bound="PostVoiceAssessmentResponse200")


@_attrs_define
class PostVoiceAssessmentResponse200:
    """
    Attributes:
        status (str | Unset): "ok" when every measure succeeded, "partial" otherwise.
        filename (str | Unset): Echo of the filename parameter.
        label (str | Unset): Echo of the label parameter.
        language (str | Unset): Echo of the language parameter.
        age (int | Unset): Echo of the age parameter, or null.
        gender (str | Unset): Echo of the gender parameter, or null.
        reference_text (str | Unset): Echo of the reference_text parameter, or null.
        audio (PostVoiceAssessmentResponse200Audio | Unset): object - {vowel, speech}, each {duration_seconds,
            sample_rate: 16000, channels: 1} or null.
        summary (PostVoiceAssessmentResponse200Summary | Unset): object - Key results: avqi, avqi_cpps,
            jitter_local_percent, shimmer_local_percent, mean_f0_hz, hnr_db, cpp_db, gne, h1_h2_db, abi, the severities
            (jitter, shimmer, hnr, cpp, breathiness) and abnormal_flags [{measure, severity}]. A key is absent when its
            measure failed.
        details (PostVoiceAssessmentResponse200Details | Unset): object - Raw result of every underlying measure, keyed
            by measure (jitter_shimmer, cpp, gne, hnr, h1_h2, formants, spectral, voice_dynamics, gemaps, pitch, intensity,
            speech_percentage, speech_segments, avqi, abi, pronunciation).
        errors (PostVoiceAssessmentResponse200Errors | Unset): object - Failed measures: {measure: {message, status}}.
        warnings (list[PostVoiceAssessmentResponse200WarningsItem] | Unset): array - Warnings (strings).
        pipeline_version (str | Unset): Pipeline version, e.g. "voice-assessment@1.0.0".
        processed_at (datetime.datetime | Unset): ISO 8601 timestamp of the analysis.
        processing_time_ms (float | Unset): number - Processing time in milliseconds.
    """

    status: str | Unset = UNSET
    filename: str | Unset = UNSET
    label: str | Unset = UNSET
    language: str | Unset = UNSET
    age: int | Unset = UNSET
    gender: str | Unset = UNSET
    reference_text: str | Unset = UNSET
    audio: PostVoiceAssessmentResponse200Audio | Unset = UNSET
    summary: PostVoiceAssessmentResponse200Summary | Unset = UNSET
    details: PostVoiceAssessmentResponse200Details | Unset = UNSET
    errors: PostVoiceAssessmentResponse200Errors | Unset = UNSET
    warnings: list[PostVoiceAssessmentResponse200WarningsItem] | Unset = UNSET
    pipeline_version: str | Unset = UNSET
    processed_at: datetime.datetime | Unset = UNSET
    processing_time_ms: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        filename = self.filename

        label = self.label

        language = self.language

        age = self.age

        gender = self.gender

        reference_text = self.reference_text

        audio: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.to_dict()

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        pipeline_version = self.pipeline_version

        processed_at: str | Unset = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        processing_time_ms = self.processing_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if filename is not UNSET:
            field_dict["filename"] = filename
        if label is not UNSET:
            field_dict["label"] = label
        if language is not UNSET:
            field_dict["language"] = language
        if age is not UNSET:
            field_dict["age"] = age
        if gender is not UNSET:
            field_dict["gender"] = gender
        if reference_text is not UNSET:
            field_dict["reference_text"] = reference_text
        if audio is not UNSET:
            field_dict["audio"] = audio
        if summary is not UNSET:
            field_dict["summary"] = summary
        if details is not UNSET:
            field_dict["details"] = details
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if pipeline_version is not UNSET:
            field_dict["pipeline_version"] = pipeline_version
        if processed_at is not UNSET:
            field_dict["processed_at"] = processed_at
        if processing_time_ms is not UNSET:
            field_dict["processing_time_ms"] = processing_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_voice_assessment_response_200_audio import (
            PostVoiceAssessmentResponse200Audio,
        )
        from ..models.post_voice_assessment_response_200_details import (
            PostVoiceAssessmentResponse200Details,
        )
        from ..models.post_voice_assessment_response_200_errors import (
            PostVoiceAssessmentResponse200Errors,
        )
        from ..models.post_voice_assessment_response_200_summary import (
            PostVoiceAssessmentResponse200Summary,
        )
        from ..models.post_voice_assessment_response_200_warnings_item import (
            PostVoiceAssessmentResponse200WarningsItem,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        filename = d.pop("filename", UNSET)

        label = d.pop("label", UNSET)

        language = d.pop("language", UNSET)

        age = d.pop("age", UNSET)

        gender = d.pop("gender", UNSET)

        reference_text = d.pop("reference_text", UNSET)

        _audio = d.pop("audio", UNSET)
        audio: PostVoiceAssessmentResponse200Audio | Unset
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = PostVoiceAssessmentResponse200Audio.from_dict(_audio)

        _summary = d.pop("summary", UNSET)
        summary: PostVoiceAssessmentResponse200Summary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = PostVoiceAssessmentResponse200Summary.from_dict(_summary)

        _details = d.pop("details", UNSET)
        details: PostVoiceAssessmentResponse200Details | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PostVoiceAssessmentResponse200Details.from_dict(_details)

        _errors = d.pop("errors", UNSET)
        errors: PostVoiceAssessmentResponse200Errors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = PostVoiceAssessmentResponse200Errors.from_dict(_errors)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[PostVoiceAssessmentResponse200WarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = PostVoiceAssessmentResponse200WarningsItem.from_dict(
                    warnings_item_data
                )

                warnings.append(warnings_item)

        pipeline_version = d.pop("pipeline_version", UNSET)

        _processed_at = d.pop("processed_at", UNSET)
        processed_at: datetime.datetime | Unset
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = isoparse(_processed_at)

        processing_time_ms = d.pop("processing_time_ms", UNSET)

        post_voice_assessment_response_200 = cls(
            status=status,
            filename=filename,
            label=label,
            language=language,
            age=age,
            gender=gender,
            reference_text=reference_text,
            audio=audio,
            summary=summary,
            details=details,
            errors=errors,
            warnings=warnings,
            pipeline_version=pipeline_version,
            processed_at=processed_at,
            processing_time_ms=processing_time_ms,
        )

        post_voice_assessment_response_200.additional_properties = d
        return post_voice_assessment_response_200

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
