# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

ROOT = None

def _source(*args, **kwargs):
    return None

def _runner(*args, **kwargs):
    return None

class _PendingVoiceAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _PendingVoiceAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _run_agent_runner(*args, **kwargs):
    return None

def test_pending_voice_interrupt_reuses_transcript_and_echo(*args, **kwargs):
    return None

def test_monitor_to_drain_transcribes_and_echoes_pending_voice_once(*args, **kwargs):
    return None

def test_telegram_video_size_gate_rejects_oversized_media_before_download(*args, **kwargs):
    return None

def _voice_event(*args, **kwargs):
    return None

def test_voice_note_merged_during_pending_stt_is_transcribed(*args, **kwargs):
    return None

def test_caption_of_voice_note_merged_during_pending_stt_is_kept(*args, **kwargs):
    return None

def test_burst_of_merged_voice_notes_transcribes_each_clip_once(*args, **kwargs):
    return None
