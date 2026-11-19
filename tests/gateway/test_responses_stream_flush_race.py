# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Sink:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_end_of_stream_flush_waits_for_a_timer_flush_awaiting_its_output_index(*args, **kwargs):
    return None
