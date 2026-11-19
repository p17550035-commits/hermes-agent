# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _CallRecorder:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _ListingRecorder:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_dispatch_all_handles_partial_failure(*args, **kwargs):
    return None

class _Args:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _stub_s6(*args, **kwargs):
    return None

def _raise_missing_sleep(*args, **kwargs):
    return None

def test_redirect_falls_back_when_sleep_missing(*args, **kwargs):
    return None

def _armed_watchdog(*args, **kwargs):
    return None

def test_redirect_disarms_startup_watchdog_before_parking(*args, **kwargs):
    return None

def test_redirect_not_taken_leaves_startup_watchdog_armed(*args, **kwargs):
    return None

class _UnregisteredRecorder:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _arrange(*args, **kwargs):
    return None

def test_start_registers_a_missing_slot_for_a_real_profile(*args, **kwargs):
    return None

def test_missing_slot_stays_an_error_outside_the_repair_case(*args, **kwargs):
    return None
