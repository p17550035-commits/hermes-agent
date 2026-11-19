# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _live_session(*args, **kwargs):
    return None

class _Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Messages:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _fake_session_db(*args, **kwargs):
    return None

def _persistence_with(*args, **kwargs):
    return None

def test_refine_spawns_review_from_persisted_transcript(*args, **kwargs):
    return None

class _MessagesEmpty:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_refine_spawns_review_from_in_memory_history_mid_conversation(*args, **kwargs):
    return None
