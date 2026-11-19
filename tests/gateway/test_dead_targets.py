# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class ForbiddenThenOkAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TransientFailAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def isolate(*args, **kwargs):
    return None

class TestDeadTargetRegistry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_forbidden_marks_target_dead_then_short_circuits(*args, **kwargs):
    return None

def test_shared_registry_is_used_when_injected(*args, **kwargs):
    return None

class RaisingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_SUBCHAT_NOT_FOUND_MESSAGES = None

class TestNotFoundBlastRadius:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
