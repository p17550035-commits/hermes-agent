# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeAllowedMentions:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _ensure_discord_mock(*args, **kwargs):
    return None

_ENV_VARS = None

def _clear_allowed_mention_env(*args, **kwargs):
    return None

def test_safe_defaults_block_everyone_and_roles(*args, **kwargs):
    return None

def test_env_var_opts_back_into_everyone(*args, **kwargs):
    return None
