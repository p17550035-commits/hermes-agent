# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

log = None

class ScopedLockDirUnusable:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def unusable_lock_dir(*args, **kwargs):
    return None

def unusable_lock_dir_recovered(*args, **kwargs):
    return None

def reset_unusable_lock_dir_reports(*args, **kwargs):
    return None

def unusable_lock_dir_reported(*args, **kwargs):
    return None
