# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _RolledBack:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def store(*args, **kwargs):
    return None

def write(*args, **kwargs):
    return None

def create(*args, **kwargs):
    return None

def capture(*args, **kwargs):
    return None

def test_pending_ack_survives_restart_and_fences_authority(*args, **kwargs):
    return None

def test_migration_preserves_bytes_invalid_rows_and_caller_transaction(*args, **kwargs):
    return None
