# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SESSION_KEY = None

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _CardAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FellThroughIntercept:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _event(*args, **kwargs):
    return None

def _clear_clarify_state(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _dispatch(*args, **kwargs):
    return None

def test_thread_prose_not_swallowed_by_native_multi_choice_clarify(*args, **kwargs):
    return None

def test_thread_prose_retires_the_native_card_before_falling_through(*args, **kwargs):
    return None

def test_typed_selection_retires_the_native_card_with_the_answer(*args, **kwargs):
    return None

def test_thread_prose_does_not_overwrite_concurrent_button_choice(*args, **kwargs):
    return None

def test_native_multi_select_out_of_range_keeps_clarify_pending(*args, **kwargs):
    return None

def test_native_multi_select_bad_comma_list_keeps_clarify_pending(*args, **kwargs):
    return None

def test_native_multi_select_prose_releases_clarify_before_routing(*args, **kwargs):
    return None

def test_prose_still_accepted_after_other_flips_text_capture(*args, **kwargs):
    return None
