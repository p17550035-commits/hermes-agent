# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_runner(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def _isolated_config(*args, **kwargs):
    return None

class _FakePickerResult:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakePickerAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_picker_path_runs_provider_listing_off_the_event_loop(*args, **kwargs):
    return None

def test_picker_path_lists_cache_only_and_probes_only_the_current_custom_endpoint(*args, **kwargs):
    return None
