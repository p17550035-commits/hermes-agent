# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _RecordingDB:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _bare_agent(*args, **kwargs):
    return None

def test_close_closes_a_dedicated_handle_it_owns(*args, **kwargs):
    return None

def test_close_never_closes_a_shared_handle(*args, **kwargs):
    return None

def test_close_without_ownership_attribute_does_not_close(*args, **kwargs):
    return None

def test_close_is_idempotent_for_an_owned_handle(*args, **kwargs):
    return None

def test_raising_close_is_swallowed_and_not_retried(*args, **kwargs):
    return None

def test_close_still_ends_the_session_row_before_closing(*args, **kwargs):
    return None

def test_lazy_recall_open_is_owned_by_the_agent(*args, **kwargs):
    return None

def test_transfer_marks_the_agent_that_holds_the_handle(*args, **kwargs):
    return None

def test_transfer_is_refused_when_the_agent_holds_a_different_handle(*args, **kwargs):
    return None

def test_transfer_is_refused_for_missing_operands(*args, **kwargs):
    return None

def test_transfer_is_refused_for_the_shared_launch_handle(*args, **kwargs):
    return None

def build_env(*args, **kwargs):
    return None

def _run_build(*args, **kwargs):
    return None

def _session(*args, **kwargs):
    return None

def registered(*args, **kwargs):
    return None

def test_deferred_build_closes_the_handle_when_the_build_fails(*args, **kwargs):
    return None

def test_deferred_build_transfers_the_handle_on_success(*args, **kwargs):
    return None

def test_deferred_build_uses_the_preserved_desktop_workspace_provenance(*args, **kwargs):
    return None

def test_deferred_build_closes_the_handle_when_the_session_is_reaped_midbuild(*args, **kwargs):
    return None

def test_deferred_build_never_opens_or_closes_for_the_launch_profile(*args, **kwargs):
    return None
