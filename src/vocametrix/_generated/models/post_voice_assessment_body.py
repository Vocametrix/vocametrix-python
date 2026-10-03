from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostVoiceAssessmentBody")


@_attrs_define
class PostVoiceAssessmentBody:
    """
    Attributes:
        language (str): REQUIRED. Language of the recordings: "fr" or "en" (selects the AVQI version and the
            pronunciation locale).
        vowel (File | Unset): Sustained vowel recording (e.g. /a/ for at least 3 seconds). Optional, but at least one of
            vowel or speech is required.
        speech (File | Unset): Connected speech recording (e.g. a reading passage). Optional, but at least one of vowel
            or speech is required.
        age (int | Unset): Patient age in years. Optional, but required when 'vowel' is sent.
        gender (str | Unset): Patient gender: "male", "female" or "other". Optional, but required when 'vowel' is sent.
        reference_text (str | Unset): Text read in the speech recording. Optional; when given, a pronunciation
            assessment is added.
        label (str | Unset): Free label returned as is. Optional.
        filename (str | Unset): Free file name returned as is. Optional.
    """

    language: str
    vowel: File | Unset = UNSET
    speech: File | Unset = UNSET
    age: int | Unset = UNSET
    gender: str | Unset = UNSET
    reference_text: str | Unset = UNSET
    label: str | Unset = UNSET
    filename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        vowel: FileTypes | Unset = UNSET
        if not isinstance(self.vowel, Unset):
            vowel = self.vowel.to_tuple()

        speech: FileTypes | Unset = UNSET
        if not isinstance(self.speech, Unset):
            speech = self.speech.to_tuple()

        age = self.age

        gender = self.gender

        reference_text = self.reference_text

        label = self.label

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
            }
        )
        if vowel is not UNSET:
            field_dict["vowel"] = vowel
        if speech is not UNSET:
            field_dict["speech"] = speech
        if age is not UNSET:
            field_dict["age"] = age
        if gender is not UNSET:
            field_dict["gender"] = gender
        if reference_text is not UNSET:
            field_dict["reference_text"] = reference_text
        if label is not UNSET:
            field_dict["label"] = label
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("language", (None, str(self.language).encode(), "text/plain")))

        if not isinstance(self.vowel, Unset):
            files.append(("vowel", self.vowel.to_tuple()))

        if not isinstance(self.speech, Unset):
            files.append(("speech", self.speech.to_tuple()))

        if not isinstance(self.age, Unset):
            files.append(("age", (None, str(self.age).encode(), "text/plain")))

        if not isinstance(self.gender, Unset):
            files.append(("gender", (None, str(self.gender).encode(), "text/plain")))

        if not isinstance(self.reference_text, Unset):
            files.append(
                ("reference_text", (None, str(self.reference_text).encode(), "text/plain"))
            )

        if not isinstance(self.label, Unset):
            files.append(("label", (None, str(self.label).encode(), "text/plain")))

        if not isinstance(self.filename, Unset):
            files.append(("filename", (None, str(self.filename).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language")

        _vowel = d.pop("vowel", UNSET)
        vowel: File | Unset
        if isinstance(_vowel, Unset):
            vowel = UNSET
        else:
            vowel = File(payload=BytesIO(_vowel))

        _speech = d.pop("speech", UNSET)
        speech: File | Unset
        if isinstance(_speech, Unset):
            speech = UNSET
        else:
            speech = File(payload=BytesIO(_speech))

        age = d.pop("age", UNSET)

        gender = d.pop("gender", UNSET)

        reference_text = d.pop("reference_text", UNSET)

        label = d.pop("label", UNSET)

        filename = d.pop("filename", UNSET)

        post_voice_assessment_body = cls(
            language=language,
            vowel=vowel,
            speech=speech,
            age=age,
            gender=gender,
            reference_text=reference_text,
            label=label,
            filename=filename,
        )

        post_voice_assessment_body.additional_properties = d
        return post_voice_assessment_body

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
