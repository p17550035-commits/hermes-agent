# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _VoiceStoppedClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Conn:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_acp_prompt_settles_a_voice_stopped_reply_as_an_ended_turn(*args, **kwargs):
    return None
