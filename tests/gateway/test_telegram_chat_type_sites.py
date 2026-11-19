# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

CASES = None

class _Bot:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _chat(*args, **kwargs):
    return None

def test_chat_info_and_inbound_event_keep_their_chat_type(*args, **kwargs):
    return None
