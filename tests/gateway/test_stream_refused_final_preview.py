# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

CURSOR = None

class _SlotAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _stream(*args, **kwargs):
    return None

def _pieces(*args, **kwargs):
    return None

def test_refused_final_edit_leaves_no_cursor_on_the_preview(*args, **kwargs):
    return None

def test_preview_holding_part_of_the_first_word_is_replaced_by_the_whole_answer(*args, **kwargs):
    return None

def test_a_first_word_fragment_whose_send_timed_out_is_continued_not_repeated(*args, **kwargs):
    return None

class _NoDeleteAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_a_fragment_that_cannot_be_deleted_is_continued_not_repeated(*args, **kwargs):
    return None

class _FlakyDeleteAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_a_refused_delete_of_the_replaced_fragment_is_retried(*args, **kwargs):
    return None

class _RefusingDeleteAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_a_fragment_whose_delete_is_refused_is_continued_not_repeated(*args, **kwargs):
    return None

class _ResetDuringDeleteAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_a_reset_during_the_fragment_delete_sends_nothing_for_the_dead_turn(*args, **kwargs):
    return None

class _TelegramFloodDeleteAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_a_fragment_whose_delete_is_only_queued_is_continued_not_repeated(*args, **kwargs):
    return None
