import json
from pathlib import Path
from src.config.paths import PROJECT_ROOT

class OutputWriter:
    @staticmethod
    def save_json(relative_path: str, data: dict):

        path = PROJECT_ROOT / relative_path
        Path(path).parent.mkdir(parents=True, exist_ok=True)

        # 데이터 문자열 예외 처리
        if isinstance(data, str):
            print("===== BEFORE LOADS =====")
            print(data[:100])

            try:
                data = json.loads(data)

                print("===== AFTER LOADS =====")
                print(type(data))

            except Exception as e:
                print("===== LOADS FAIL =====")
                print(e)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def write_file(relative_path: str, content: str):

        path = PROJECT_ROOT / relative_path

        Path(path).parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)