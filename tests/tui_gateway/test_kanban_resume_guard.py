# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_original_stdout = None

def _restore_stdout(*args, **kwargs):
    return None

def server(*args, **kwargs):
    return None

class _KanbanDB:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _resume(*args, **kwargs):
    return None

def test_gateway_resume_refuses_kanban_worker_session(*args, **kwargs):
    return None

def test_gateway_resume_ordinary_session_unchanged(*args, **kwargs):
    return None
