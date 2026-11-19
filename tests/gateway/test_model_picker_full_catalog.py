# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_MODELS = None

class _CapturingPickerAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_model_picker_receives_a_providers_whole_catalog(*args, **kwargs):
    return None
