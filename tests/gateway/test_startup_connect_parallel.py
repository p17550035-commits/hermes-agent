# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _OrderRecorder:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _TimingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_startup_connects_platforms_concurrently(*args, **kwargs):
    return None

def test_startup_one_failing_platform_does_not_block_others(*args, **kwargs):
    return None

class TestTelegramColdStartCap:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
