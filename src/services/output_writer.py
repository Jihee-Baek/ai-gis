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
            
            # 마크다운 코드 블록 제거
            clean_data = data.strip()
            if clean_data.startswith("```"):
                lines = clean_data.split("\n")
                if lines[0].startswith("```"):
                    lines = lines[1:]
                if lines[-1].startswith("```"):
                    lines = lines[:-1]
                clean_data = "\n".join(lines).strip()

            try:
                data = json.loads(clean_data)
                print("===== AFTER LOADS =====")
            except Exception as e:
                print("===== LOADS FAIL =====")
                print(e)
                # 파싱 실패 시 원본 문자열이라도 저장 시도 (또는 에러 처리)


        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def write_file(relative_path: str, content: str):

        path = PROJECT_ROOT / relative_path

        Path(path).parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)