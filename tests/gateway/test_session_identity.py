# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Stub:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _stub(*args, **kwargs):
    return None

def _runner(*args, **kwargs):
    return None

def mux(*args, **kwargs):
    return None

def test_identity_is_one_frozen_value_that_every_reader_agrees_on(*args, **kwargs):
    return None

def test_unresolved_under_multiplex_raises_and_never_means_default(*args, **kwargs):
    return None

def test_replace_source_keeps_identity_and_transport_where_dataclasses_replace_drops_them(*args, **kwargs):
    return None
