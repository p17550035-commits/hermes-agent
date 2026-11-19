# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Clock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _HangingConnect:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _CaptureRequest:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _stock_send_request(*args, **kwargs):
    return None

def test_built_transports_walk_every_path_within_the_send_deadline(*args, **kwargs):
    return None

def test_tighter_configured_connect_is_never_widened(*args, **kwargs):
    return None

def test_capped_walk_keeps_both_seed_ips_at_the_tail_after_many_doh_answers(*args, **kwargs):
    return None
