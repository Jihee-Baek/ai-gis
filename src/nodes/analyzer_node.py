import os
import json
from src.services.gemini_executor import GeminiExecutor

def code_analyzer_node(state):
    print("=" * 20, "Start code_analyzer_node")

    # 프로젝트 소스코드 목록 및 핵심 파일 내용 추출
    project_summary = []
    project_path = "./project"
    
    if not os.path.exists(project_path):
        print(f"Error: Project path {project_path} not found.")
        return {"analysis_report": {"error": "Project path not found"}}

    for root, dirs, files in os.walk(project_path):
        if "node_modules" in dirs:
            dirs.remove("node_modules")
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        
        for file in files:
            if file.endswith(('.py', '.tsx', '.ts', '.sql')):
                file_path = os.path.join(root, file)
                project_summary.append(file_path)

    file_list_str = "\n".join(project_summary)

    prompt = f"""
당신은 Senior Code Analyzer입니다. 
다음 프로젝트 파일 목록을 보고, 현재 구현된 시스템의 핵심 스펙(API 엔드포인트, 데이터베이스 테이블, 주요 프론트엔드 컴포넌트)을 요약하여 JSON 형태로 추출하세요.

# Project Files
{file_list_str}

# Output Format (JSON)
{{
  "implemented_apis": [],
  "database_tables": [],
  "frontend_features": [],
  "detected_changes": "기존 설계와 비교하여 변경된 사항 요약"
}}

Return JSON only.
"""
    response = GeminiExecutor.run(prompt)
    
    # 마크다운 코드 블록 제거 (```json ... ```)
    clean_json = response.strip()
    if clean_json.startswith("```"):
        lines = clean_json.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines[-1].startswith("```"):
            lines = lines[:-1]
        clean_json = "\n".join(lines).strip()

    try:
        analysis_report = json.loads(clean_json)
    except Exception as e:
        print(f"JSON Parsing Error in code_analyzer_node: {e}")
        analysis_report = {"error": "Failed to parse analysis report", "raw": response}

    return {"analysis_report": analysis_report}
