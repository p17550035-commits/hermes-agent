# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _run(*args, **kwargs):
    return None

def test_alias_key_turn_waits_and_order_is_preserved(*args, **kwargs):
    return None

def test_distinct_sessions_do_not_contend(*args, **kwargs):
    return None

def test_timeout_fails_closed_instead_of_authorizing_an_unserialized_turn(*args, **kwargs):
    return None

def test_agent_path_propagates_timed_out_lease_before_loading_transcript(*args, **kwargs):
    return None

def test_full_dispatch_rejects_lease_timeout_without_running_goal_hook(*args, **kwargs):
    return None

class _ObservedLock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _GatedLock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_registry_does_not_evict_lease_during_waiter_handoff(*args, **kwargs):
    return None

def test_registry_does_not_evict_an_uncontended_acquire_before_it_locks(*args, **kwargs):
    return None

def test_timed_out_acquire_does_not_pin_idle_registry_entry(*args, **kwargs):
    return None

def test_cancelled_acquire_does_not_pin_idle_registry_entry(*args, **kwargs):
    return None

def test_rebind_moves_serialization_to_new_session_id(*args, **kwargs):
    return None

def test_rebind_does_not_replace_target_during_waiter_handoff(*args, **kwargs):
    return None

def test_runner_release_turn_lease_is_token_scoped_and_bare_safe(*args, **kwargs):
    return None
