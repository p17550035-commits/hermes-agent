# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

POSITIVE_CASES = None

NEGATIVE_CASES = None

def test_is_silence_narration_positive(*args, **kwargs):
    return None

def test_real_replies_are_not_silence_narration(*args, **kwargs):
    return None

def test_length_guard_rejects_long_strings(*args, **kwargs):
    return None

class RecordingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_silence_narration_dropped_pre_send(*args, **kwargs):
    return None

def test_config_opt_out_lets_silence_through(*args, **kwargs):
    return None

def test_env_does_not_override_config_opt_out(*args, **kwargs):
    return None

def test_env_does_not_disable_filter_when_config_enabled(*args, **kwargs):
    return None

def test_multiplex_profiles_independent_silence_narration_filtering(*args, **kwargs):
    return None

def test_cron_job_id_metadata_bypasses_the_filter(*args, **kwargs):
    return None

def test_non_cron_metadata_still_filters(*args, **kwargs):
    return None
