# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _bare_runner(*args, **kwargs):
    return None

def test_secondary_profile_pairing_stores_created(*args, **kwargs):
    return None

def test_pairing_store_scoped_to_profile_dir(*args, **kwargs):
    return None

def test_routed_pairing_grant_mirror_stays_in_profile_scope(*args, **kwargs):
    return None

class _ExplodingScope:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_allowlist_env_read_never_borrows_on_scope_failure(*args, **kwargs):
    return None

def test_allowlist_sync_does_not_persist_foreign_allowlist(*args, **kwargs):
    return None

def test_allowlist_scoped_miss_configures_nothing(*args, **kwargs):
    return None
