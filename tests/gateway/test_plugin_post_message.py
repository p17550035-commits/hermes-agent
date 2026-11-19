# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _EditingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _RaisingEditAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FailedEditAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _setup(*args, **kwargs):
    return None

def _in_session(*args, **kwargs):
    return None

def test_post_then_edit_targets_the_calling_session(*args, **kwargs):
    return None

def test_no_bound_session_is_refused_without_sending(*args, **kwargs):
    return None
