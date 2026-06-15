from pathlib import Path
from src.config.paths import PROJECT_ROOT

class PromptLoader:
    @staticmethod
    def load(relative_path: str) -> str:
        path = PROJECT_ROOT / relative_path
        return Path(path).read_text(encoding="utf-8")