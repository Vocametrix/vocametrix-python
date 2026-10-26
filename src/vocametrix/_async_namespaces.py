"""Async namespace classes for AsyncVocametrixClient."""

from __future__ import annotations

from typing import Any, AsyncIterator, Dict, Optional

import httpx

from ._http import (
    AudioInput,
    request_with_retry_async,
    upload_assign_file_id_async,
    upload_blob_url_async,
    sse_stream_async,
)
from ._namespaces import TranscriptionEvent, transcript_text
from ._response_types import (
    AbiResult,
    AvqiResult,
    CppResult,
    DsiResult,
    EgemapsResult,
    FormantStatisticsResult,
    GneResult,
    H1H2Result,
    HnrResult,
    JitterShimmerResult,
    PhonemeResult,
    PronunciationResult,
    ProsodySimilarityResult,
    SoundLevelResult,
    SpectralResult,
    SzRatioResult,
    TtsResult,
    VoiceDynamicsResult,
    DdkResult,
    VrpResult,
)


class AsyncAvqiNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(
        self,
        sustained_vowel: AudioInput,
        connected_speech: AudioInput,
        version: str = "v03.01",
        email: Optional[str] = None,
    ) -> AvqiResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        cs_id = await upload_assign_file_id_async(self._c, self._base, connected_speech, effective_email)
        params: Dict[str, str] = {"svFileId": sv_id, "csFileId": cs_id, "version": version}
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-avqi", params=params)
        return resp.json()


class AsyncDsiNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(
        self,
        sustained_vowel: AudioInput,
        mpt: float,
        maximum_f0: float,
        minimum_intensity: float,
        age: int,
        gender: int,
        email: Optional[str] = None,
    ) -> DsiResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(
            self._c, "GET", f"{self._base}/api/calculate-dsi",
            params={
                "svFileId": sv_id, "mpt": mpt, "maximumF0": maximum_f0,
                "minimumIntensity": minimum_intensity, "age": age, "gender": gender,
            },
        )
        return resp.json()


class AsyncCppNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> CppResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-cpp", params={"svFileId": sv_id})
        return resp.json()


class AsyncHnrNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, age: int, gender: int = 1, email: Optional[str] = None) -> HnrResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-hnr-multiband", params={"svFileId": sv_id, "age": age, "gender": gender})
        return resp.json()


class AsyncJitterShimmerNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> JitterShimmerResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/jitter-shimmer", params={"svFileId": sv_id})
        return resp.json()


class AsyncVrpNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, age: int = 30, gender: int = 1, email: Optional[str] = None) -> VrpResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-ambitus", params={"svFileId": sv_id, "age": age, "gender": gender})
        return resp.json()


class AsyncPronunciationNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str) -> None:
        self._c = client
        self._base = base_url

    async def assess(self, audio: AudioInput, reference_text: str, locale: str = "en-US") -> PronunciationResult:
        blob_url = await upload_blob_url_async(self._c, self._base, audio)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/pronunciation-assessment",
            json={"blobURL": blob_url, "referenceText": reference_text, "locale": locale},
        )
        return resp.json()


class AsyncTranscriptionNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, api_key: str) -> None:
        self._c = client
        self._base = base_url
        self._key = api_key

    async def stream(self, audio: AudioInput, locale: str = "en-US") -> AsyncIterator[TranscriptionEvent]:
        blob_url = await upload_blob_url_async(self._c, self._base, audio)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/offline-speech-to-text",
            json={"blobURL": blob_url, "locale": locale},
        )
        transcription_id: str = resp.json()["transcriptionId"]
        async for payload in sse_stream_async(self._base, transcription_id, self._key):
            event = TranscriptionEvent(
                status=payload.get("status", ""),
                progress=payload.get("progress"),
                display_text=payload.get("displayText"),
                raw=payload,
            )
            if event.is_terminal_success:
                async with httpx.AsyncClient(timeout=60.0) as http:
                    transcript = (await http.get(payload["contentUrl"])).json()
                event.status = "Succeeded"
                event.display_text = transcript_text(transcript)
            yield event


class AsyncTtsNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str) -> None:
        self._c = client
        self._base = base_url

    async def synthesize(self, text: str, locale: str = "en-US", voice_name: Optional[str] = None) -> TtsResult:
        body: Dict[str, Any] = {"text": text, "language": locale}
        if voice_name:
            body["voice"] = voice_name
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/text-to-speech", json=body)
        return resp.json()


class AsyncPhonemeNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def detect(self, audio: AudioInput, language: str = "fr-FR", email: Optional[str] = None) -> PhonemeResult:
        effective_email = email if email is not None else self._default_email
        file_id = await upload_assign_file_id_async(self._c, self._base, audio, effective_email)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/analyze-phonemes-live",
            json={"fileId": file_id, "language": language},
        )
        return resp.json()


class AsyncStutteringNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def classify(
        self,
        audio: AudioInput,
        email: Optional[str] = None,
        poll_interval: float = 5.0,
        timeout: float = 620.0,
    ) -> Dict[str, Any]:
        import asyncio
        from .exceptions import VocametrixServerError

        effective_email = email if email is not None else self._default_email
        file_id = await upload_assign_file_id_async(self._c, self._base, audio, effective_email)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/classify-stuttering",
            json={"fileId": file_id},
        )
        session_id: str = resp.json()["session_id"]

        elapsed = 0.0
        while elapsed < timeout:
            await asyncio.sleep(poll_interval)
            elapsed += poll_interval
            status_r = await request_with_retry_async(self._c, "GET", f"{self._base}/api/therapy-status/{session_id}")
            payload = status_r.json()
            state = payload.get("status", payload.get("state", ""))
            if state in ("completed", "succeeded", "done"):
                break
            if state in ("failed", "error"):
                raise VocametrixServerError(f"Stuttering classification failed: {payload}")
        else:
            raise VocametrixServerError(f"Stuttering classification timed out after {timeout}s (session={session_id})")

        result_r = await request_with_retry_async(self._c, "GET", f"{self._base}/api/therapy-result/{session_id}")
        return result_r.json()


class AsyncProsodyNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def similarity(self, model: AudioInput, learner: AudioInput, email: Optional[str] = None) -> ProsodySimilarityResult:
        effective_email = email if email is not None else self._default_email
        model_id = await upload_assign_file_id_async(self._c, self._base, model, effective_email)
        user_id = await upload_assign_file_id_async(self._c, self._base, learner, effective_email)
        resp = await request_with_retry_async(
            self._c, "GET", f"{self._base}/api/calculate-prosody-similarity",
            params={"modelFileId": model_id, "userFileId": user_id},
        )
        return resp.json()


class AsyncEgemapsNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def extract(self, audio: AudioInput, email: Optional[str] = None) -> EgemapsResult:
        effective_email = email if email is not None else self._default_email
        file_id = await upload_assign_file_id_async(self._c, self._base, audio, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/gemaps-extract", params={"fileId": file_id})
        return resp.json()


class AsyncSoundLevelNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str) -> None:
        self._c = client
        self._base = base_url

    async def measure(self, audio: AudioInput, start_sec: float = 0.001, end_sec: Optional[float] = None) -> SoundLevelResult:
        if start_sec == 0.0:
            from .exceptions import VocametrixValidationError
            raise VocametrixValidationError(
                "start_sec=0 is rejected by the backend (treated as falsy). "
                "Pass start_sec=0.001 as the minimum offset."
            )
        blob_url = await upload_blob_url_async(self._c, self._base, audio)
        # stop_sec is required; a value past the end of the file means "to the end".
        body: Dict[str, Any] = {
            "blobUrl": blob_url, "start_sec": start_sec,
            "stop_sec": end_sec if end_sec is not None else 999999,
        }
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/soundLevel", json=body)
        return resp.json()


class AsyncAdvancedVoiceAnalysisNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate_h1h2(self, sustained_vowel: AudioInput, gender: int = 1, email: Optional[str] = None) -> H1H2Result:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-h1-h2", params={"svFileId": sv_id, "gender": gender})
        return resp.json()

    async def calculate_spectral(self, sustained_vowel: AudioInput, age: int, gender: int = 1, email: Optional[str] = None) -> SpectralResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-spectral-advanced", params={"svFileId": sv_id, "age": age, "gender": gender})
        return resp.json()

    async def calculate_sz_ratio(self, sustained_s: AudioInput, sustained_z: AudioInput, patient_age: int, gender: int = 1, email: Optional[str] = None) -> SzRatioResult:
        effective_email = email if email is not None else self._default_email
        s_id = await upload_assign_file_id_async(self._c, self._base, sustained_s, effective_email)
        z_id = await upload_assign_file_id_async(self._c, self._base, sustained_z, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-sz-ratio", params={"sFileId": s_id, "zFileId": z_id, "patientAge": patient_age, "gender": gender})
        return resp.json()

    async def calculate_gne(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> GneResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-gne", params={"svFileId": sv_id})
        return resp.json()

    async def calculate_formant_statistics(self, sustained_vowel: AudioInput, age: int, gender: int = 1, email: Optional[str] = None) -> FormantStatisticsResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-formant-statistics", params={"svFileId": sv_id, "age": age, "gender": gender})
        return resp.json()

    async def calculate_abi(self, sustained_vowel: AudioInput, connected_speech: AudioInput, email: Optional[str] = None) -> AbiResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        cs_id = await upload_assign_file_id_async(self._c, self._base, connected_speech, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-abi", params={"svFileId": sv_id, "csFileId": cs_id})
        return resp.json()

    async def calculate_voice_dynamics(self, sustained_vowel: AudioInput, age: int, gender: int = 1, email: Optional[str] = None) -> VoiceDynamicsResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-voice-dynamics", params={"svFileId": sv_id, "age": age, "gender": gender})
        return resp.json()

    async def measure_ddk(self, audio: AudioInput, task: str, gender: Optional[str] = None, age: Optional[int] = None, email: Optional[str] = None) -> DdkResult:
        effective_email = email if email is not None else self._default_email
        file_id = await upload_assign_file_id_async(self._c, self._base, audio, effective_email)
        params: Dict[str, Any] = {"fileId": file_id, "task": task}
        if gender is not None:
            params["gender"] = gender
        if age is not None:
            params["age"] = age
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/measure-ddk", params=params)
        return resp.json()


class AsyncAiAgentsNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str) -> None:
        self._c = client
        self._base = base_url

    async def therapy_plan(self, session_metadata: Dict[str, Any], wav2vec_output: Dict[str, Any]) -> Dict[str, Any]:
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/therapy-planning-agent", json={"sessionMetadata": session_metadata, "wav2vecOutput": wav2vec_output})
        return resp.json()

    async def speech_exercise(self, patient_profile: Dict[str, Any], difficulty: str = "medium") -> Dict[str, Any]:
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/speech-exercise-generator", json={"patientProfile": patient_profile, "difficulty": difficulty})
        return resp.json()

    async def syntax_check(self, text: str, language: str = "en") -> Dict[str, Any]:
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/syntax-checker-agent", json={"text": text, "language": language})
        return resp.json()

    async def spell_check(self, text: str, language: str = "en") -> Dict[str, Any]:
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/spell-agent", json={"text": text, "language": language})
        return resp.json()

    async def interpret_metrics(self, metrics: Dict[str, Any], praat_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        body: Dict[str, Any] = {"metrics": metrics}
        if praat_results is not None:
            body["praatResults"] = praat_results
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/voice-metrics-interpreter", json=body)
        return resp.json()

    async def adaptive_exercise(self, patient_id: str, session_history: list) -> Dict[str, Any]:
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/adaptive-exercise-agent", json={"patientId": patient_id, "sessionHistory": session_history})
        return resp.json()

    async def french_to_ipa(self, phonetic_input: list) -> Dict[str, Any]:
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/french-to-ipa-agent", json={"phoneticInput": phonetic_input})
        return resp.json()

    async def word_list(self, target_phoneme: str, difficulty: str = "medium", locale: str = "en-US") -> Dict[str, Any]:
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/word-list-generator", json={"targetPhoneme": target_phoneme, "difficulty": difficulty, "locale": locale})
        return resp.json()

    async def therapist_assistant(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        body: Dict[str, Any] = {"query": query}
        if context is not None:
            body["context"] = context
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/speech-therapist-assistant", json=body)
        return resp.json()
