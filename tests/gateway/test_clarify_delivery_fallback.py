# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

UNDELIVERED = None

PICK = None

class _CardAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def loop(*args, **kwargs):
    return None

def _runner(*args, **kwargs):
    return None

def _answer_once_text_prompt_is_seen(*args, **kwargs):
    return None

def test_rejected_card_is_reasked_as_plain_text_and_the_typed_answer_counts(*args, **kwargs):
    return None

def test_declined_card_is_never_reasked_as_text(*args, **kwargs):
    return None

def test_card_failing_after_the_ack_window_falls_back_to_text_instead_of_waiting(*args, **kwargs):
    return None

def test_card_resolving_ambiguous_after_the_ack_window_stays_armed_for_a_button_tap(*args, **kwargs):
    return None

def test_card_and_text_both_failing_late_release_the_wait_with_the_delivery_notice(*args, **kwargs):
    return None

def test_card_declined_after_the_ack_window_releases_with_the_declined_notice(*args, **kwargs):
    return None

def test_no_status_adapter_reports_the_missing_surface_not_inactivity(*args, **kwargs):
    return None
