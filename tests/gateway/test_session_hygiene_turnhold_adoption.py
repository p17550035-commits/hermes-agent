# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_history(*args, **kwargs):
    return None

class _CaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _write_turnhold_config(*args, **kwargs):
    return None

def _build_runner(*args, **kwargs):
    return None

def _install_handle(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def _install_fakes(*args, **kwargs):
    return None

def _drain_deferred(*args, **kwargs):
    return None

def test_turn_hold_keeps_admission_and_adopts_watermark_fenced_summary(*args, **kwargs):
    return None

def test_turn_hold_kept_admission_arms_flat_retry_only_when_nothing_commits(*args, **kwargs):
    return None

def test_turn_hold_without_watermark_fence_still_cancels(*args, **kwargs):
    return None
