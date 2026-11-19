# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

ALPHABET = None

CODE_LENGTH = None

CODE_TTL_SECONDS = None

RATE_LIMIT_SECONDS = None

LOCKOUT_SECONDS = None

MAX_PENDING_PER_PLATFORM = None

MAX_FAILED_ATTEMPTS = None

DECLINE_DEDUPE_SECONDS = None

PAIRING_DIR = None

def _default_pairing_dir(*args, **kwargs):
    return None

def _allowlist_env_for_platform(*args, **kwargs):
    return None

def _split_allowlist(*args, **kwargs):
    return None

def _platform_uses_whatsapp_identity(*args, **kwargs):
    return None

def _normalize_user_id(*args, **kwargs):
    return None

def _user_id_aliases(*args, **kwargs):
    return None

def _user_ids_match(*args, **kwargs):
    return None

def _matching_ids(*args, **kwargs):
    return None

def _read_allowlist_env(*args, **kwargs):
    return None

def _configured_allowlist(*args, **kwargs):
    return None

def _write_allowlist_env(*args, **kwargs):
    return None

def _sync_allowlist_add(*args, **kwargs):
    return None

def _iter_live_gateway_adapters(*args, **kwargs):
    return None

def _adapter_platform_name(*args, **kwargs):
    return None

def _purge_allowlist_entries(*args, **kwargs):
    return None

def _sync_live_adapter_allowlist_remove(*args, **kwargs):
    return None

def _sync_allowlist_remove(*args, **kwargs):
    return None

def _load_json_file(*args, **kwargs):
    return None

def _read_pending_strict(*args, **kwargs):
    return None

def _save_json_file(*args, **kwargs):
    return None

def _migrate_split_pairing_dirs(*args, **kwargs):
    return None

_dir_lock_holders_guard = None

def _dir_lock_holder(*args, **kwargs):
    return None

def _is_hashed_entry(*args, **kwargs):
    return None

def _entry_created_at(*args, **kwargs):
    return None

class PairingStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
