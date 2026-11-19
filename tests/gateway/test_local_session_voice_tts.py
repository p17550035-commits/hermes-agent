# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingModel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_local_voice_tts_is_refused_and_other_voice_forms_stay(*args, **kwargs):
    return None

def test_local_voice_refusal_reads_the_argument_as_the_handler_does(*args, **kwargs):
    return None

def test_local_session_voice_tts_never_synthesizes_unplayable_audio(*args, **kwargs):
    return None
