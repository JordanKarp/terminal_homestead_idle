from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Settings:
    show_all: bool = True
    achievements: List[str] = field(default_factory=list)
    autosave: bool = False
    autosave_interval: int = 10

    def to_dict(self) -> Dict[str, Any]:
        return {
            "show_all": self.show_all,
            "achievements": list(self.achievements),
            "autosave": self.autosave,
            "autosave_interval": int(self.autosave_interval),
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Settings":
        s = Settings()
        if not isinstance(data, dict):
            return s
        s.show_all = bool(data.get("show_all", s.show_all))
        s.achievements = list(data.get("achievements", s.achievements))
        s.autosave = bool(data.get("autosave", s.autosave))
        try:
            s.autosave_interval = int(data.get("autosave_interval", s.autosave_interval))
        except Exception:
            s.autosave_interval = s.autosave_interval
        return s
