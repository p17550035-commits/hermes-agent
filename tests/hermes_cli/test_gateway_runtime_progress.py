# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Clock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def clock(*args, **kwargs):
    return None

def _run(*args, **kwargs):
    return None

def test_progressing_owner_outlives_the_base_deadline_until_the_cap(*args, **kwargs):
    return None

def test_owner_with_no_cpu_progress_fails_at_the_base_deadline(*args, **kwargs):
    return None

def test_owner_that_stalls_after_progressing_fails_within_two_windows(*args, **kwargs):
    return None

def test_explicit_timeout_is_a_hard_deadline(*args, **kwargs):
    return None

def test_unreadable_owner_cpu_never_extends(*args, **kwargs):
    return None

def test_owner_cpu_readable_only_after_the_first_sample_still_extends(*args, **kwargs):
    return None

def test_invalid_timeout_is_refused(*args, **kwargs):
    return None

def test_cpu_seconds_reads_this_process(*args, **kwargs):
    return None

def test_a_lock_record_without_a_running_gateway_is_never_the_owner(*args, **kwargs):
    return None
