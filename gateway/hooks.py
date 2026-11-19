# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

HOOKS_DIR = None

_HOOKS_DIR_AT_IMPORT = None

def _resolve_hooks_dir(*args, **kwargs):
    return None

def _skip(*args, **kwargs):
    return None

def _load_hook_dir(*args, **kwargs):
    return None

class HookRegistry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ProfileHookRegistries:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
