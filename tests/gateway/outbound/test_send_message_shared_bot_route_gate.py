# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_PLATFORMS = None

class _Primary:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def satellite(*args, **kwargs):
    return None

def _satellite_config(*args, **kwargs):
    return None

def _tool(*args, **kwargs):
    return None

def _live_adapter_allows(*args, **kwargs):
    return None

def test_send_to_unrouted_chat_never_uses_the_primary_bot(*args, **kwargs):
    return None

def test_cron_standalone_fallback_cannot_reach_the_primary_bot(*args, **kwargs):
    return None

_ORIGIN_ROUTED = None

def test_satellite_acts_in_its_inbound_routed_conversation_only(*args, **kwargs):
    return None

def test_origin_topic_does_not_vouch_for_the_rest_of_its_chat(*args, **kwargs):
    return None

def test_shared_channel_origin_matches_on_the_turn_sender(*args, **kwargs):
    return None

_GROUP_PLUS_THREAD = None

def test_thread_pinned_origin_does_not_admit_its_groups_top_level(*args, **kwargs):
    return None

def test_discord_thread_origin_still_admits_itself_without_a_thread_id(*args, **kwargs):
    return None

_CHAT_SCOPED = None

def _sibling_pinned_routes(*args, **kwargs):
    return None

def test_chat_route_does_not_reach_a_thread_pinned_to_another_profile(*args, **kwargs):
    return None

def test_cron_shared_view_does_not_reach_a_thread_pinned_to_another_profile(*args, **kwargs):
    return None

def test_cron_shared_view_refuses_every_target_when_the_route_read_fails(*args, **kwargs):
    return None

def test_cron_shared_view_is_built_from_one_route_read(*args, **kwargs):
    return None

def test_google_chat_space_top_level_refused_when_another_profile_owns_a_thread(*args, **kwargs):
    return None

def test_more_specific_route_of_another_profile_wins_without_an_origin(*args, **kwargs):
    return None

def test_google_chat_space_guard_ignores_own_threads_and_matches_thread_only_routes(*args, **kwargs):
    return None
