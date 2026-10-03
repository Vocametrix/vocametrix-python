from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostClassifyFrenchPlosiveBody")


@_attrs_define
class PostClassifyFrenchPlosiveBody:
    """
    Attributes:
        audio (str): Mode 1 (use ONE of audio/blobUrl/fileId). Direct audio file upload, multipart/form-data — the field
            name MUST be exactly `audio`.
        blob_url (str): Mode 2 (use ONE of audio/blobUrl/fileId), JSON body. HTTPS URL of the audio file, downloaded
            server-side.
        file_id (str): Mode 3 (use ONE of audio/blobUrl/fileId), JSON body. fileId from a prior /api/assignFileId
            upload.
        expected_plosive (str | Unset): Optional (also accepted as expectedPlosive, any input mode). When provided, the
            response is scored against this plosive.
    """

    audio: str
    blob_url: str
    file_id: str
    expected_plosive: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio = self.audio

        blob_url = self.blob_url

        file_id = self.file_id

        expected_plosive = self.expected_plosive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audio": audio,
                "blobUrl": blob_url,
                "fileId": file_id,
            }
        )
        if expected_plosive is not UNSET:
            field_dict["expected_plosive"] = expected_plosive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio = d.pop("audio")

        blob_url = d.pop("blobUrl")

        file_id = d.pop("fileId")

        expected_plosive = d.pop("expected_plosive", UNSET)

        post_classify_french_plosive_body = cls(
            audio=audio,
            blob_url=blob_url,
            file_id=file_id,
            expected_plosive=expected_plosive,
        )

        post_classify_french_plosive_body.additional_properties = d
        return post_classify_french_plosive_body

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
