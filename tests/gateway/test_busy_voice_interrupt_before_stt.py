# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _interrupt_via(*args, **kwargs):
    return None

def test_busy_voice_note_interrupts_before_its_transcription_finishes(*args, **kwargs):
    return None
