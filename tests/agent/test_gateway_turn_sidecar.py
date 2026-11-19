# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeTodoStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeGuardrails:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _build(*args, **kwargs):
    return None

def _stub_runtime_main(*args, **kwargs):
    return None

RESET_NOTE = None

VC_NOTE = None

class TestConsumeIsOneShot:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestStringContentSidecarDelivery:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMultimodalFallback:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
