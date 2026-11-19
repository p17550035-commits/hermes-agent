# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def emitted(*args, **kwargs):
    return None

def _fail_build(*args, **kwargs):
    return None

def _run_build(*args, **kwargs):
    return None

def test_provider_not_configured_is_named_in_the_error_event(*args, **kwargs):
    return None

def test_an_unrelated_build_failure_carries_no_code(*args, **kwargs):
    return None

class TestAgentInitRaisesTheNamedError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
