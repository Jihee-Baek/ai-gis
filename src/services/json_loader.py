import json
from src.config.paths import PROJECT_ROOT

class JsonLoader:

    @staticmethod
    def load(relative_path: str):

        file_path = PROJECT_ROOT /relative_path

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)