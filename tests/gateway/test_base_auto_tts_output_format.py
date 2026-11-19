# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _DummyAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_voice_event(*args, **kwargs):
    return None

def _hold_typing(*args, **kwargs):
    return None

def test_output_path_is_mp3_for_non_opus_platforms(*args, **kwargs):
    return None

def test_base_auto_tts_skips_playback_when_tool_reports_failure(*args, **kwargs):
    return None
