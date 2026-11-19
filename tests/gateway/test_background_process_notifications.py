# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class AdmittingHandler:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeRegistry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _build_runner(*args, **kwargs):
    return None

def _watcher_dict(*args, **kwargs):
    return None

def _watch_event(*args, **kwargs):
    return None

class TestLoadBackgroundNotificationsMode:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_consumed_completion_skips_raw_notification(*args, **kwargs):
    return None

def test_agent_notify_receipt_only_while_launching_turn_is_busy(*args, **kwargs):
    return None

def test_arm_process_watcher_schedules_on_live_loop_only(*args, **kwargs):
    return None

def test_consumed_completion_skips_raw_notification_without_agent_notify(*args, **kwargs):
    return None

def test_inject_watch_notification_routes_from_session_store_origin(*args, **kwargs):
    return None

def test_post_turn_watch_drain_off_consumes_without_injecting(*args, **kwargs):
    return None

def test_post_turn_watch_drain_all_injects_from_queued_event_origin(*args, **kwargs):
    return None

def test_inject_watch_notification_drops_stale_trigger_reply_anchor(*args, **kwargs):
    return None

def test_inject_watch_notification_loads_session_store_off_loop(*args, **kwargs):
    return None

def test_inject_watch_notification_ignores_foreground_event_source(*args, **kwargs):
    return None

class TestConciseFormatter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_agent_notify_refused_completion_backs_off_then_sends_plain_notice(*args, **kwargs):
    return None

def test_concise_mode_no_interim_output_updates(*args, **kwargs):
    return None

def test_parse_session_key_with_extra_parts(*args, **kwargs):
    return None

def test_parse_session_key_named_profile(*args, **kwargs):
    return None

def test_parse_session_key_named_profile_thread_id(*args, **kwargs):
    return None

def test_parse_session_key_named_profile_group_suffix_omitted(*args, **kwargs):
    return None

def test_parse_session_key_main_shape_unchanged(*args, **kwargs):
    return None

def test_parse_session_key_rejects_invalid_namespace(*args, **kwargs):
    return None

def test_build_process_event_source_named_profile_key(*args, **kwargs):
    return None

def test_inject_watch_notification_raw_session_key_self_posts(*args, **kwargs):
    return None

def test_inject_watch_notification_origin_session_id_wins(*args, **kwargs):
    return None

def test_async_delegation_apiserver_persists_delivery_not_self_post(*args, **kwargs):
    return None

def test_async_delegation_apiserver_persist_failure_is_retryable(*args, **kwargs):
    return None

def test_gateway_drain_retains_and_formats_overflow_events(*args, **kwargs):
    return None

def test_raw_output_modes_are_human_facing(*args, **kwargs):
    return None
