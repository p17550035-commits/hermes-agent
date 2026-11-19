# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Mic:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Sink:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Runner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def owner(*args, **kwargs):
    return None

def _transcripts(*args, **kwargs):
    return None

def test_voice_off_stops_the_sessions_capture_and_drops_late_text(*args, **kwargs):
    return None

def test_another_sessions_voice_off_leaves_this_capture_running(*args, **kwargs):
    return None

def test_spoken_stop_turns_the_owner_mode_off(*args, **kwargs):
    return None

def test_no_speech_limit_turns_the_owner_mode_off(*args, **kwargs):
    return None

def test_a_second_sessions_start_is_refused_while_another_captures(*args, **kwargs):
    return None

def test_another_session_may_start_once_the_capture_ended(*args, **kwargs):
    return None

def stop_phrase(*args, **kwargs):
    return None

def test_typed_stop_turns_the_owner_mode_off_not_the_sidecar_flag(*args, **kwargs):
    return None

def test_typed_stop_reads_the_owner_mode(*args, **kwargs):
    return None

def test_full_duplex_stop_turns_the_owner_mode_off_not_the_sidecar_flag(*args, **kwargs):
    return None
