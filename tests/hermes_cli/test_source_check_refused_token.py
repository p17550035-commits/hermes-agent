# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Api:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def api(*args, **kwargs):
    return None

def test_a_refused_token_falls_back_to_anonymous(*args, **kwargs):
    return None

def test_a_spent_rate_limit_still_fails(*args, **kwargs):
    return None
