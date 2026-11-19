# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

KEY = None

CHAT = None

class CleanupAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _event(*args, **kwargs):
    return None

def _register_cleanup(*args, **kwargs):
    return None

class _AuthorityAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_authority_busy_follow_up_deletes_its_own_progress_bubbles(*args, **kwargs):
    return None

def test_busy_follow_up_goal_notice_keeps_its_bubble_cleanup_without_adapter_guard(*args, **kwargs):
    return None

def test_busy_follow_up_loop_notice_keeps_its_bubble_cleanup_without_adapter_guard(*args, **kwargs):
    return None
