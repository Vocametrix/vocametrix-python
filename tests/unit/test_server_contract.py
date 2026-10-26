"""Parameters each endpoint requires.

Checked against routes/audio/praat.service.js and audio.controller.js in
vocametrix-platform. A missing or misnamed parameter is a 400 from the server,
which a mocked transport would otherwise never show.
"""

import json

import httpx
import pytest
import respx

from vocametrix import AsyncVocametrixClient, VocametrixClient

BASE = "https://platform.vocametrix.com"


@pytest.fixture
def wav(tmp_path):
    p = tmp_path / "a.wav"
    p.write_bytes(b"RIFF" + b"\x00" * 40)
    return str(p)


@pytest.fixture
def client():
    c = VocametrixClient(api_key="test-key")
    yield c
    c.close()


def mock_file_ids(*ids):
    it = iter(ids)
    respx.post(f"{BASE}/api/assignFileId").mock(
        side_effect=lambda request: httpx.Response(200, json={"fileId": next(it)})
    )


OK = httpx.Response(200, json={})
BLOB = "https://az.example.com/blob"


def mock_blob_upload():
    urls = {"uploadURL": "https://az.example.com/put", "blobURL": BLOB}
    respx.post(f"{BASE}/api/get-blob-url").mock(return_value=httpx.Response(200, json=urls))
    respx.put("https://az.example.com/put").mock(return_value=httpx.Response(201))


def query_of(route):
    return dict(route.calls.last.request.url.params)


def body_of(route):
    return json.loads(route.calls.last.request.content)


@respx.mock
def test_avqi_sends_cs_and_version(client, wav):
    mock_file_ids("sv1", "cs1")
    route = respx.get(f"{BASE}/api/calculate-avqi").mock(return_value=OK)
    client.avqi.calculate(wav, wav)
    assert query_of(route) == {"svFileId": "sv1", "csFileId": "cs1", "version": "v03.01"}


@respx.mock
def test_dsi_sends_voice_range(client, wav):
    mock_file_ids("sv1")
    route = respx.get(f"{BASE}/api/calculate-dsi").mock(return_value=OK)
    client.dsi.calculate(wav, mpt=15.2, maximum_f0=440, minimum_intensity=45.5, age=35, gender=2)
    assert query_of(route) == {
        "svFileId": "sv1", "mpt": "15.2", "maximumF0": "440",
        "minimumIntensity": "45.5", "age": "35", "gender": "2",
    }


@respx.mock
def test_hnr_sends_age_and_gender(client, wav):
    mock_file_ids("sv1")
    route = respx.get(f"{BASE}/api/calculate-hnr-multiband").mock(return_value=OK)
    client.hnr.calculate(wav, age=40, gender=2)
    assert query_of(route) == {"svFileId": "sv1", "age": "40", "gender": "2"}


@respx.mock
def test_spectral_formants_dynamics_send_age_and_gender(client, wav):
    mock_file_ids("a", "b", "c")
    spectral = respx.get(f"{BASE}/api/calculate-spectral-advanced").mock(return_value=OK)
    formants = respx.get(f"{BASE}/api/calculate-formant-statistics").mock(return_value=OK)
    dynamics = respx.get(f"{BASE}/api/calculate-voice-dynamics").mock(return_value=OK)
    client.advanced.calculate_spectral(wav, age=40, gender=2)
    client.advanced.calculate_formant_statistics(wav, age=40, gender=2)
    client.advanced.calculate_voice_dynamics(wav, age=40, gender=2)
    assert query_of(spectral) == {"svFileId": "a", "age": "40", "gender": "2"}
    assert query_of(formants) == {"svFileId": "b", "age": "40", "gender": "2"}
    assert query_of(dynamics) == {"svFileId": "c", "age": "40", "gender": "2"}


@respx.mock
def test_ddk_sends_task_gender_age(client, wav):
    mock_file_ids("d1", "d2")
    route = respx.get(f"{BASE}/api/measure-ddk").mock(return_value=OK)
    client.advanced.measure_ddk(wav, task="pataka", gender="male", age=70)
    assert query_of(route) == {"fileId": "d1", "task": "pataka", "gender": "male", "age": "70"}
    client.advanced.measure_ddk(wav, task="pa_steady")
    assert query_of(route) == {"fileId": "d2", "task": "pa_steady"}


@respx.mock
def test_abi_sends_cs(client, wav):
    mock_file_ids("sv1", "cs1")
    route = respx.get(f"{BASE}/api/calculate-abi").mock(return_value=OK)
    client.advanced.calculate_abi(wav, wav)
    assert query_of(route) == {"svFileId": "sv1", "csFileId": "cs1"}


@respx.mock
def test_sz_ratio_sends_s_z_age_gender(client, wav):
    mock_file_ids("s1", "z1")
    route = respx.get(f"{BASE}/api/calculate-sz-ratio").mock(return_value=OK)
    client.advanced.calculate_sz_ratio(wav, wav, patient_age=50, gender=1)
    assert query_of(route) == {"sFileId": "s1", "zFileId": "z1", "patientAge": "50", "gender": "1"}


@respx.mock
def test_prosody_sends_model_and_user(client, wav):
    mock_file_ids("m1", "u1")
    route = respx.get(f"{BASE}/api/calculate-prosody-similarity").mock(return_value=OK)
    client.prosody.similarity(wav, wav)
    assert query_of(route) == {"modelFileId": "m1", "userFileId": "u1"}


@respx.mock
def test_gemaps_sends_file_id(client, wav):
    mock_file_ids("f1")
    route = respx.get(f"{BASE}/api/gemaps-extract").mock(return_value=OK)
    client.egemaps.extract(wav)
    assert query_of(route) == {"fileId": "f1"}


@respx.mock
def test_phonemes_call_analyze_phonemes_live(client, wav):
    mock_file_ids("f1")
    route = respx.post(f"{BASE}/api/analyze-phonemes-live").mock(return_value=OK)
    client.phoneme.detect(wav)
    assert body_of(route) == {"fileId": "f1", "language": "fr-FR"}


@respx.mock
def test_tts_sends_language_and_voice(client):
    route = respx.post(f"{BASE}/api/text-to-speech").mock(return_value=OK)
    client.tts.synthesize("Bonjour", locale="fr-FR", voice_name="fr-FR-DeniseNeural")
    assert body_of(route) == {"text": "Bonjour", "language": "fr-FR", "voice": "fr-FR-DeniseNeural"}


@respx.mock
def test_sound_level_sends_blob_url_and_stop_sec(client, wav):
    mock_blob_upload()
    route = respx.post(f"{BASE}/api/soundLevel").mock(return_value=OK)
    client.sound_level.measure(wav)
    assert body_of(route) == {"blobUrl": BLOB, "start_sec": 0.001, "stop_sec": 999999}


@respx.mock
def test_transcription_sends_blob_url_uppercase(client, wav, monkeypatch):
    mock_blob_upload()
    route = respx.post(f"{BASE}/api/offline-speech-to-text").mock(
        return_value=httpx.Response(200, json={"transcriptionId": "t1"})
    )
    monkeypatch.setattr("vocametrix._namespaces.sse_stream", lambda *args: iter(()))
    list(client.transcription.stream(wav, locale="fr-FR"))
    assert body_of(route) == {"blobURL": BLOB, "locale": "fr-FR"}


@respx.mock
@pytest.mark.asyncio
async def test_async_client_sends_the_same_parameters(wav):
    mock_file_ids("sv1", "cs1", "s1", "z1", "f1")
    avqi = respx.get(f"{BASE}/api/calculate-avqi").mock(return_value=OK)
    sz = respx.get(f"{BASE}/api/calculate-sz-ratio").mock(return_value=OK)
    gemaps = respx.get(f"{BASE}/api/gemaps-extract").mock(return_value=OK)
    async with AsyncVocametrixClient(api_key="test-key") as c:
        await c.avqi.calculate(wav, wav)
        await c.advanced.calculate_sz_ratio(wav, wav, patient_age=50, gender=1)
        await c.egemaps.extract(wav)
    assert query_of(avqi) == {"svFileId": "sv1", "csFileId": "cs1", "version": "v03.01"}
    assert query_of(sz) == {"sFileId": "s1", "zFileId": "z1", "patientAge": "50", "gender": "1"}
    assert query_of(gemaps) == {"fileId": "f1"}
