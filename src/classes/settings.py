from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Settings:
    """User-visible settings for the game.

    Attributes:
        show_all: Whether to show all tasks by default.
        achievements: List of unlocked achievement IDs.
        autosave: Whether autosave is enabled.
        autosave_interval: Autosave interval in minutes.
    """
    show_all: bool = True
    achievements: List[str] = field(default_factory=list)
    autosave: bool = False
    autosave_interval: int = 10

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable dict representing the settings."""
        return {
            "show_all": bool(self.show_all),
            "achievements": list(self.achievements),
            "autosave": bool(self.autosave),
            "autosave_interval": int(self.autosave_interval),
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Settings":
        """Create a Settings instance from a mapping.

        This method is defensive: if ``data`` is not a mapping or contains
        malformed values, sensible defaults are preserved.
        Accepts string values for booleans (e.g., 'true'/'false') and
        numeric strings for the autosave interval.
        """
        s = Settings()
        if not isinstance(data, dict):
            return s

        def _parse_bool(val, default: bool) -> bool:
            if isinstance(val, bool):
                return val
            if isinstance(val, str):
                v = val.strip().lower()
                if v in ("true", "1", "yes", "y", "t"):
                    return True
                if v in ("false", "0", "no", "n", "f"):
                    return False
                return default
            if isinstance(val, (int, float)):
                return bool(val)
            return default

        s.show_all = _parse_bool(data.get("show_all", s.show_all), s.show_all)

        ach = data.get("achievements", s.achievements)
        if isinstance(ach, list):
            s.achievements = [str(a) for a in ach]
        else:
            # preserve default if malformed
            s.achievements = list(s.achievements)

        s.autosave = _parse_bool(data.get("autosave", s.autosave), s.autosave)

        ai = data.get("autosave_interval", s.autosave_interval)
        try:
            s.autosave_interval = int(ai)
        except Exception:
            # keep default on any conversion failure
            s.autosave_interval = s.autosave_interval

        return s
