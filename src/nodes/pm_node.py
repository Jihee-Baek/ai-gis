from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader

def pm_node(state):
    
    print('='*20, 'Start pm_node')

    system = PromptLoader.load("agents/pm/system.md")
    rules = PromptLoader.load("agents/pm/rules.md") 
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/prd.schema.json")

    existing_prd = JsonLoader.load("outputs/prd.json")
    existing_content_prompt = ""
    if existing_prd:
        existing_content_prompt = f"""
# Existing PRD
기존에 작성된 PRD 내용입니다. 이 내용을 바탕으로 새로운 요청사항을 반영하여 업데이트하세요.
기존에 만족스러운 부분은 유지하고, 변경이 필요한 부분만 수정하거나 새로운 내용을 추가하세요.

{existing_prd}
"""

    prompt = f"""
{system}

{rules}

{language}

{output_contract}

{existing_content_prompt}

# User Request
사용자의 새로운 요청사항입니다.

{state["user_request"]}

# Output Schema
{schema}

Output must follow prd schema exactly.
Return JSON only.
"""
    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/prd.json", response)

    state["prd_path"] = "outputs/prd.json"

    return {
        "prd_path":
        "outputs/prd.json"
    }