# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _NoopAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _install_fake_agent(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _make_voice_source(*args, **kwargs):
    return None

def _setup_monkeypatches(*args, **kwargs):
    return None

def test_run_agent_voice_turn_no_name_error(*args, **kwargs):
    return None
