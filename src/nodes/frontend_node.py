import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader


def frontend_node(state):

    print('='*20, 'Start frontend_node')

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])

    system = PromptLoader.load("agents/frontend/system.md")
    rules = PromptLoader.load("agents/frontend/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/frontend_design.schema.json")

    prompt = f"""
{system}

{rules}

{language}

{output_contract}

# PRD
{json.dumps(prd, ensure_ascii=False, indent=2)}

# Architecture
{json.dumps(architecture, ensure_ascii=False, indent=2)}

# Output Schema
{schema}

Output must follow frontend schema exactly.
Return JSON only.
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/frontend_design.json", response)

    state["frontend_design_path"] = "outputs/frontend_design.json"

    return {
        "frontend_design_path":
        "outputs/frontend_design.json"

    }