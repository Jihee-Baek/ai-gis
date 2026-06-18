import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader

def frontend_codegen_node(state):
    print("=" * 20, "Start frontend_codegen_node")

    if not state.get("frontend_structure_path"):
        print("Skipping frontend_codegen_node: frontend_structure_path not found")
        return state

    prd = JsonLoader.load(state["prd_path"]) if state.get("prd_path") else {}
    architecture = JsonLoader.load(state["architecture_path"]) if state.get("architecture_path") else {}
    frontend_structure = JsonLoader.load(state["frontend_structure_path"])


    system = PromptLoader.load("agents/frontend_codegen/system.md")
    rules = PromptLoader.load("agents/frontend_codegen/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/frontend_codegen.schema.json")

    existing_codegen = JsonLoader.load("outputs/frontend_codegen.json")
    existing_content_prompt = ""
    if existing_codegen:
        # 파일이 너무 크면 요약 정보만 전달 (토큰 절약 및 에러 방지)
        file_list = [f["path"] for f in existing_codegen.get("generated_files", [])]
        existing_content_prompt = f"""
# Existing Frontend Files
이미 생성된 파일 목록입니다: {file_list}
기존 코드를 바탕으로 수정이 필요한 부분만 업데이트하세요.
"""

    prompt = f"""
{system}

{rules}

{language}

{output_contract}

{existing_content_prompt}

Read the following files:

# PRD
{json.dumps(prd, ensure_ascii=False, indent=2)}

# Architecture
{json.dumps(architecture, ensure_ascii=False, indent=2)}

# frontend_structure
{json.dumps(frontend_structure, ensure_ascii=False, indent=2)}

# User Request
사용자의 새로운 요청사항입니다.

{state["user_request"]}

# Output Schema
{schema}

Output must follow frontend codegen exactly.
Return JSON only.

Generate:
outputs/frontend_codegen.json
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/frontend_codegen.json", response)

    state["frontend_codegen_path"] = "outputs/frontend_codegen.json"

    return {
        "frontend_codegen_path":
        "outputs/frontend_codegen.json"
    }