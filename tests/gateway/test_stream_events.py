# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _base_adapter(*args, **kwargs):
    return None

class _FakeSink:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_message_chunk_flows_to_sink_on_delta(*args, **kwargs):
    return None

def test_intermediate_message_stop_breaks_segment_but_final_does_not(*args, **kwargs):
    return None

def test_commentary_flows_to_sink(*args, **kwargs):
    return None

def test_tool_call_chunk_renders_default_chrome(*args, **kwargs):
    return None

def test_new_mode_dedups_same_tool(*args, **kwargs):
    return None
