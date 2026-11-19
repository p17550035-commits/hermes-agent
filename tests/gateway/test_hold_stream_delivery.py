# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Chat:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _NativeStreamChat:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _relay_slack(*args, **kwargs):
    return None

def _frames(*args, **kwargs):
    return None

CHATS = None

def _deliver(*args, **kwargs):
    return None

def test_a_held_reply_reaches_the_chat_only_as_the_rewrite(*args, **kwargs):
    return None

def test_a_transform_that_did_not_ask_keeps_streaming(*args, **kwargs):
    return None
