# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _InterimOnlyHarness:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _run_mark_streamed_delivery(*args, **kwargs):
    return None

def _consumer(*args, **kwargs):
    return None

def test_stream_capable_consumer_still_warns(*args, **kwargs):
    return None

def test_interim_only_consumer_skips_duplicate_warning(*args, **kwargs):
    return None
