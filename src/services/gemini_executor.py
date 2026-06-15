import subprocess

NODE_EXE = r"C:\Users\modim\anaconda3\envs\gemini_env\node.exe"

GEMINI_JS = r"C:\Users\modim\anaconda3\envs\gemini_env\node_modules\@google\gemini-cli\bundle\gemini.js"


class GeminiExecutor:

    @staticmethod
    def run(prompt: str) -> str:

        result = subprocess.run(
            [
                NODE_EXE,
                GEMINI_JS,
                "--prompt",
                prompt
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        print("RETURN CODE:", result.returncode)
        print("STDERR:", result.stderr)

        if result.returncode != 0:
            raise Exception(
                f"Gemini CLI Error\n{result.stderr}"
            )

        return result.stdout