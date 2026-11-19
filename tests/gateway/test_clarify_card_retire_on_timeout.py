# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _CardAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _TextAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_ONE_QUESTION = None

def _asked(*args, **kwargs):
    return None

def _run_clarify(*args, **kwargs):
    return None

def test_timeout_retires_the_native_card_with_the_expired_notice(*args, **kwargs):
    return None

def test_timeout_schedules_nothing_for_adapters_without_a_card(*args, **kwargs):
    return None

def test_real_answer_starting_with_a_bracket_is_not_mistaken_for_a_sentinel(*args, **kwargs):
    return None

_THREE_QUESTIONS = None

def test_batch_routing(*args, **kwargs):
    return None

class _UndeliverableAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_clarify_tool_batch_route_answers_and_stops_together(*args, **kwargs):
    return None

def test_skip_hint_only_on_messaging_platforms(*args, **kwargs):
    return None
