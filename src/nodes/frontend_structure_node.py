import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader

def frontend_structure_node(state):
    print("=" * 20, "Start frontend_structure_node")

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])
    frontend_design = JsonLoader.load(state["frontend_design_path"])


    system = PromptLoader.load("agents/frontend_structure/system.md")
    rules = PromptLoader.load("agents/frontend_structure/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/frontend_structure.schema.json")

    existing_structure = JsonLoader.load("outputs/frontend_structure.json")
    existing_content_prompt = ""
    if existing_structure:
        existing_content_prompt = f"""
# Existing Frontend Structure
기존에 작성된 프론트엔드 구조 설계 내용입니다. 이 내용을 바탕으로 새로운 설계 변경사항을 반영하여 업데이트하세요.
기존에 만족스러운 부분은 유지하고, 변경이 필요한 부분만 수정하거나 새로운 내용을 추가하세요.

{existing_structure}
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

# Frontend_design
{json.dumps(frontend_design, ensure_ascii=False, indent=2)}

# User Request
사용자의 새로운 요청사항입니다.

{state["user_request"]}

# Output Schema
{schema}

Output must follow front structure exactly.
Return JSON only.

Generate:
outputs/frontend_structure.json
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/frontend_structure.json", response)

    state["frontend_structure_path"] = "outputs/frontend_structure.json"

    return {
        "frontend_structure_path":
        "outputs/frontend_structure.json"
    }