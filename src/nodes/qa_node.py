import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader


def qa_node(state):

    print('='*20, 'Start qa_node')

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])
    backend = JsonLoader.load(state["backend_design_path"])
    frontend = JsonLoader.load(state["frontend_design_path"])
    reviewer = JsonLoader.load(state["reviewer_path"])
    devops = JsonLoader.load(state["devops_plan_path"])

    system = PromptLoader.load("agents/qa/system.md")
    rules = PromptLoader.load("agents/qa/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/test_plan.schema.json")

    existing_plan = JsonLoader.load("outputs/test_plan.json")
    existing_content_prompt = ""
    if existing_plan:
        existing_content_prompt = f"""
# Existing Test Plan
기존에 수립된 테스트 계획 내용입니다. 이 내용을 바탕으로 새로운 설계 및 DevOps 계획을 반영하여 업데이트하세요.
기존에 유효한 테스트 시나리오는 유지하고, 새로운 기능이나 변경된 로직에 대한 테스트 케이스를 추가하세요.

{existing_plan}
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

# Backend
{json.dumps(backend, ensure_ascii=False, indent=2)}

# Frontend
{json.dumps(frontend, ensure_ascii=False, indent=2)}

# Reviewer
{json.dumps(reviewer, ensure_ascii=False, indent=2)}

# Devops
{json.dumps(devops, ensure_ascii=False, indent=2)}

# User Request
사용자의 새로운 요청사항입니다.

{state["user_request"]}

# Output Schema
{schema}

Output must follow test_plan schema exactly.
Return JSON only.
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/test_plan.json", response)

    state["test_plan_path"] = "outputs/test_plan.json"
    
    return {
        "test_plan_path":
        "outputs/test_plan.json"
    }