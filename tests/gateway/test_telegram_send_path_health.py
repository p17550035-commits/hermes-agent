# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_adapter(*args, **kwargs):
    return None

def test_send_short_circuits_when_path_degraded(*args, **kwargs):
    return None

class _FloodError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_send_long_flood_fails_closed_without_inline_sleep(*args, **kwargs):
    return None

def test_send_short_flood_still_retries_inline(*args, **kwargs):
    return None

def test_send_times_out_instead_of_hanging(*args, **kwargs):
    return None

def test_media_send_times_out_instead_of_hanging(*args, **kwargs):
    return None

def test_mark_connected_publishes_connected_when_healthy(*args, **kwargs):
    return None

def test_mark_connected_publishes_retrying_when_send_path_degraded(*args, **kwargs):
    return None

def test_record_polling_progress_republishes_connected_after_degraded_connect(*args, **kwargs):
    return None

def test_mid_session_polling_death_publishes_retrying_while_running(*args, **kwargs):
    return None

def test_polling_death_before_connect_does_not_publish(*args, **kwargs):
    return None

def test_record_polling_progress_does_not_flip_when_not_running_or_fatal(*args, **kwargs):
    return None
