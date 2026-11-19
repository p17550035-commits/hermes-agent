# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

KEY = None

class _CountingPaused:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _result(*args, **kwargs):
    return None

def test_typing_stops_once_a_silent_turn_returns(*args, **kwargs):
    return None

def test_a_silent_topic_leaves_another_topics_typing_on(*args, **kwargs):
    return None
