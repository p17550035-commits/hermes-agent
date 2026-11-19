# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

ACP_MAX_MODELS_PER_PROVIDER = None

def _named_custom_provider_catalogs(*args, **kwargs):
    return None

def _semantic_provider(*args, **kwargs):
    return None

def _empty_catalog_applies(*args, **kwargs):
    return None

def _choice_provider(*args, **kwargs):
    return None

def encode_model_choice(*args, **kwargs):
    return None

def fallback_model_state(*args, **kwargs):
    return None

class _ModelCatalog:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def build_model_state(*args, **kwargs):
    return None
