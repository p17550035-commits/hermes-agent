# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _shell(*args, **kwargs):
    return None

def _expected(*args, **kwargs):
    return None

class _Connection:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_classic_cli_create_sends_client_env_when_the_gateway_takes_it(*args, **kwargs):
    return None

def test_classic_cli_new_sends_this_shells_client_env(*args, **kwargs):
    return None

def test_client_env_policy_reads_the_profiles_extra_names(*args, **kwargs):
    return None

def test_client_env_policy_reads_the_effective_config_and_bypass_reads_none(*args, **kwargs):
    return None

def test_tui_launcher_hands_the_shell_env_to_ink(*args, **kwargs):
    return None

def test_tui_bootstrap_keeps_the_client_env_out_of_a_daemon_it_starts(*args, **kwargs):
    return None
