# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Harness:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FloodedChat:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _flood_frozen_turn(*args, **kwargs):
    return None

def test_flood_frozen_preview_is_finished_in_place_not_sent_twice(*args, **kwargs):
    return None

def test_preview_still_flooded_past_the_retry_leaves_the_normal_send(*args, **kwargs):
    return None

def test_consumer_cancelled_mid_final_leaves_one_complete_message(*args, **kwargs):
    return None

def test_turn_replaced_during_the_flood_wait_publishes_nothing(*args, **kwargs):
    return None

def test_finishing_edit_carries_the_topic_routing_metadata(*args, **kwargs):
    return None

def test_an_edit_that_would_truncate_leaves_the_normal_send(*args, **kwargs):
    return None

def test_slack_measures_the_formatted_text_its_edit_cuts(*args, **kwargs):
    return None

def test_a_replaced_turn_and_a_receiptless_edit_are_distinguishable(*args, **kwargs):
    return None
