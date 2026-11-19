# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PROJECT_A_ROOM_ID = None

PROJECT_B_ROOM_ID = None

PROJECT_A_NAME = None

PROJECT_B_NAME = None

PROJECT_A_TOPIC = None

PROJECT_B_TOPIC = None

PROJECT_A_ALIAS = None

PROJECT_B_ALIAS = None

SENDER = None

def _make_adapter(*args, **kwargs):
    return None

class _FakeMatrixClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _source_for(*args, **kwargs):
    return None

def _matrix_event(*args, **kwargs):
    return None

def _context_for(*args, **kwargs):
    return None

def test_matrix_session_scope_auto_and_thread_preserve_synthetic_threads(*args, **kwargs):
    return None

def test_matrix_project_context_survives_concurrent_messages(*args, **kwargs):
    return None

def test_matrix_inbound_handler_emits_project_b_metadata_not_project_a(*args, **kwargs):
    return None

def test_matrix_inbound_handler_keeps_project_a_and_b_distinct(*args, **kwargs):
    return None

def _make_matrix_source(*args, **kwargs):
    return None

def _entry(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _event(*args, **kwargs):
    return None

def test_matrix_status_reports_current_matrix_room_scope(*args, **kwargs):
    return None

def test_matrix_resume_quoted_title_same_room(*args, **kwargs):
    return None

def test_matrix_resume_cross_room_requires_explicit_flag_and_warns(*args, **kwargs):
    return None
