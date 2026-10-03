from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateCsidResponse200")


@_attrs_define
class GetCalculateCsidResponse200:
    """
    Attributes:
        csid_score (float | Unset): number - CSID score (154.59 − 10.393·CPP − 1.083·SR − 3.713·SR_SD).
        cpp (float | Unset): number - Smoothed cepstral peak prominence over the whole signal, in dB.
        sr (float | Unset): number - Low/high spectral ratio (energy below 4 kHz vs 4–8 kHz), in dB, averaged over
            voiced frames.
        sr_sd (float | Unset): number - Standard deviation of the spectral ratio across voiced frames, in dB.
        n_voiced_frames (int | Unset): integer - Number of voiced frames used.
        cutoff_screening (float | Unset): number - Screening cut-off (19.09).
        cutoff_balanced (float | Unset): number - Balanced cut-off (24.27).
        cutoff_conservative (float | Unset): number - Conservative cut-off (30.85).
        csid_reference (str | Unset): Bibliographic reference of the formula (Awan et al.).
        csid_caveat (str | Unset): Note on the per-frame approximation used by this implementation.
    """

    csid_score: float | Unset = UNSET
    cpp: float | Unset = UNSET
    sr: float | Unset = UNSET
    sr_sd: float | Unset = UNSET
    n_voiced_frames: int | Unset = UNSET
    cutoff_screening: float | Unset = UNSET
    cutoff_balanced: float | Unset = UNSET
    cutoff_conservative: float | Unset = UNSET
    csid_reference: str | Unset = UNSET
    csid_caveat: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csid_score = self.csid_score

        cpp = self.cpp

        sr = self.sr

        sr_sd = self.sr_sd

        n_voiced_frames = self.n_voiced_frames

        cutoff_screening = self.cutoff_screening

        cutoff_balanced = self.cutoff_balanced

        cutoff_conservative = self.cutoff_conservative

        csid_reference = self.csid_reference

        csid_caveat = self.csid_caveat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csid_score is not UNSET:
            field_dict["CSID_SCORE"] = csid_score
        if cpp is not UNSET:
            field_dict["CPP"] = cpp
        if sr is not UNSET:
            field_dict["SR"] = sr
        if sr_sd is not UNSET:
            field_dict["SR_SD"] = sr_sd
        if n_voiced_frames is not UNSET:
            field_dict["N_VOICED_FRAMES"] = n_voiced_frames
        if cutoff_screening is not UNSET:
            field_dict["CUTOFF_SCREENING"] = cutoff_screening
        if cutoff_balanced is not UNSET:
            field_dict["CUTOFF_BALANCED"] = cutoff_balanced
        if cutoff_conservative is not UNSET:
            field_dict["CUTOFF_CONSERVATIVE"] = cutoff_conservative
        if csid_reference is not UNSET:
            field_dict["CSID_REFERENCE"] = csid_reference
        if csid_caveat is not UNSET:
            field_dict["CSID_CAVEAT"] = csid_caveat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        csid_score = d.pop("CSID_SCORE", UNSET)

        cpp = d.pop("CPP", UNSET)

        sr = d.pop("SR", UNSET)

        sr_sd = d.pop("SR_SD", UNSET)

        n_voiced_frames = d.pop("N_VOICED_FRAMES", UNSET)

        cutoff_screening = d.pop("CUTOFF_SCREENING", UNSET)

        cutoff_balanced = d.pop("CUTOFF_BALANCED", UNSET)

        cutoff_conservative = d.pop("CUTOFF_CONSERVATIVE", UNSET)

        csid_reference = d.pop("CSID_REFERENCE", UNSET)

        csid_caveat = d.pop("CSID_CAVEAT", UNSET)

        get_calculate_csid_response_200 = cls(
            csid_score=csid_score,
            cpp=cpp,
            sr=sr,
            sr_sd=sr_sd,
            n_voiced_frames=n_voiced_frames,
            cutoff_screening=cutoff_screening,
            cutoff_balanced=cutoff_balanced,
            cutoff_conservative=cutoff_conservative,
            csid_reference=csid_reference,
            csid_caveat=csid_caveat,
        )

        get_calculate_csid_response_200.additional_properties = d
        return get_calculate_csid_response_200

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
