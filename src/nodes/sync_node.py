import json
from src.services.json_loader import JsonLoader
from src.services.output_writer import OutputWriter
from src.services.gemini_executor import GeminiExecutor

def doc_sync_node(state):
    print("=" * 20, "Start doc_sync_node")

    analysis_report = state.get("analysis_report")
    if not analysis_report:
        return {"sync_status": False}

    # 기존 architecture.json 로드
    existing_arch = JsonLoader.load("outputs/architecture.json")
    
    prompt = f"""
당신은 Senior Architect입니다. 
코드 분석 결과(# Code Analysis Report)를 바탕으로 기존 아키텍처 설계(# Existing Architecture)를 최신화하세요.

**보수적 업데이트 원칙 (Minimal Refactoring Policy):**
1. 실제 구현과 설계서가 상충하는 지점만 '수술'하듯 정밀하게 수정하세요.
2. 실제 코드에 반영되지 않은 불필요한 아키텍처 변경이나 리팩토링은 절대 하지 마세요.
3. 기존 설계의 문구, 형식, 명칭을 가급적 토씨 하나 틀리지 않게 유지하세요.
4. 새로운 기능이 발견된 경우에만 해당 섹션에 내용을 추가하세요.

# Existing Architecture
{json.dumps(existing_arch, ensure_ascii=False, indent=2)}

# Code Analysis Report
{json.dumps(analysis_report, ensure_ascii=False, indent=2)}

최종 업데이트된 architecture.json 내용을 반환하세요.
Return JSON only.
"""
    response = GeminiExecutor.run(prompt)
    OutputWriter.save_json("outputs/architecture.json", response)

    # version.md 생성 로직 추가
    version_prompt = f"""
코드 분석 결과와 업데이트된 설계를 바탕으로 변경 사항 요약 보고서를 작성하세요.
루트 폴더의 version.md 파일에 들어갈 내용입니다.

# Analysis Report
{json.dumps(analysis_report, ensure_ascii=False, indent=2)}

형식:
## [버전] - 날짜
### 변경 사항
- 구현된 API 목록
- DB 스키마 변경 사항
- 프론트엔드 주요 변경 사항
- 기타 특이 사항

작성된 마크다운 내용만 반환하세요.
"""
    version_content = GeminiExecutor.run(version_prompt)
    OutputWriter.write_file("version.md", version_content)

    return {"sync_status": True}
