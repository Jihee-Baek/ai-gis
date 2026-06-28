import os
from google import genai
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class GeminiExecutor:

    @staticmethod
    def run(prompt: str) -> str:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY가 설정되지 않았습니다. "
                "프로젝트 루트의 .env.template 파일을 .env 파일로 복사한 뒤 "
                "Gemini API Key를 입력해주세요."
            )

        # google-genai 클라이언트 초기화
        client = genai.Client(api_key=api_key)

        # API 호출 및 텍스트 생성
        # 기본적으로 gemini-2.5-flash 모델을 사용합니다.
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text