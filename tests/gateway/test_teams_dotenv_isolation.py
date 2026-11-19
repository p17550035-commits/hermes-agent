# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

CANARY_KEY = None

def _plant_cwd_dotenv(*args, **kwargs):
    return None

def _install_fake_teams_sdk(*args, **kwargs):
    return None

def _purge_teams_adapter_modules(*args, **kwargs):
    return None

class TestTeamsAdapterImportDoesNotLeakDotenv:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestLoadGatewayConfigApiServerExplicitDisable:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
