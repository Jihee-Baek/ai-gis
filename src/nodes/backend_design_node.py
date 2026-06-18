import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader


def backend_design_node(state):

    print('='*20, 'Start backend_design_node')

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])

    system = PromptLoader.load("agents/backend/system.md")
    rules = PromptLoader.load("agents/backend/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/backend_design.schema.json")

    existing_design = JsonLoader.load("outputs/backend_design.json")
    existing_content_prompt = ""
    if existing_design:
        existing_content_prompt = f"""
# Existing Backend Design
기존에 작성된 백엔드 설계 내용입니다. 이 내용을 바탕으로 새로운 아키텍처 및 PRD 요구사항을 반영하여 업데이트하세요.
기존에 만족스러운 부분은 유지하고, 변경이 필요한 부분만 수정하거나 새로운 내용을 추가하세요.

{existing_design}
"""

    prompt = f"""
{system}

{rules}

{language}

{output_contract}

{existing_content_prompt}

# PRD
{json.dumps(prd, ensure_ascii=False, indent=2)}

# Architecture
{json.dumps(architecture, ensure_ascii=False, indent=2)}

# User Request
사용자의 새로운 요청사항입니다.

{state["user_request"]}

# Output Schema
{schema}

Output must follow backend schema exactly.
Return JSON only.
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/backend_design.json", response)

    state["backend_design_path"] = "outputs/backend_design.json"

    return {
        "backend_design_path":
        "outputs/backend_design.json"
    }