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
실제 코드로 구현된 스펙이 설계서와 다를 경우, 실제 구현을 기준으로 문서를 업데이트해야 합니다.

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
