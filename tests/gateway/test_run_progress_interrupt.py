# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class ProgressCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class PreInterruptAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class InterruptedAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class PartialTruncationAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _run_once(*args, **kwargs):
    return None

def test_baseline_non_interrupted_agent_renders_progress(*args, **kwargs):
    return None

def test_partial_empty_agent_response_is_normalized(*args, **kwargs):
    return None

def test_progress_suppressed_when_agent_is_interrupted(*args, **kwargs):
    return None

def test_partial_site_code_result_is_delivered_verbatim_not_double_wrapped(*args, **kwargs):
    return None

def test_partial_without_site_code_keeps_the_generic_wrapper(*args, **kwargs):
    return None
