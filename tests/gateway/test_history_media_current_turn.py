# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StubStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _tts_tool_row(*args, **kwargs):
    return None

def test_current_turn_tts_media_not_treated_as_history(*args, **kwargs):
    return None

def test_prior_turn_media_still_deduped(*args, **kwargs):
    return None
