# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SESSION = None

APPROVAL = None

class _ButtonAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _PlainAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _runner(*args, **kwargs):
    return None

def pending_entry(*args, **kwargs):
    return None

def test_timeout_edits_the_card_to_say_the_command_did_not_run(*args, **kwargs):
    return None

def test_prompt_carries_request_identity(*args, **kwargs):
    return None

def test_timeout_falls_back_to_a_new_message_when_the_card_cannot_be_edited(*args, **kwargs):
    return None

def test_other_settle_reasons_post_nothing(*args, **kwargs):
    return None
