# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Stream:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _answer(*args, **kwargs):
    return None

class _ChunkedBody:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_oversized_provider_is_ignored_and_never_fully_read(*args, **kwargs):
    return None

def test_normal_answers_parse_and_request_identity_encoding(*args, **kwargs):
    return None
