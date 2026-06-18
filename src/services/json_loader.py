import json
from src.config.paths import PROJECT_ROOT

class JsonLoader:

    @staticmethod
    def load(relative_path: str):

        file_path = PROJECT_ROOT / relative_path

        if not file_path.exists():
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                content = f.read().strip()
                if not content:
                    return None
                
                # Handle potential string-wrapped JSON (double encoded)
                if content.startswith('"') and content.endswith('"'):
                    try:
                        content = json.loads(content)
                    except:
                        pass
                
                # Handle potential markdown blocks
                if content.startswith("```"):
                    lines = content.split("\n")
                    if lines[0].startswith("```"): lines = lines[1:]
                    if lines[-1].startswith("```"): lines = lines[:-1]
                    content = "\n".join(lines).strip()
                
                return json.loads(content)
            except Exception as e:
                print(f"JsonLoader Error ({relative_path}): {e}")
                return None