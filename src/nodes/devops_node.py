import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader


def devops_node(state):

    print('='*20, 'Start devops_node')

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])
    backend = JsonLoader.load(state["backend_design_path"])
    frontend = JsonLoader.load(state["frontend_design_path"])
    reviewer = JsonLoader.load(state["reviewer_path"])

    system = PromptLoader.load("agents/devops/system.md")
    rules = PromptLoader.load("agents/devops/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/devops_plan.schema.json")

    prompt = f"""
{system}

{rules}

{language}

{output_contract}

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

# Output Schema
{schema}

Output must follow devops_plan schema exactly.
Return JSON only.
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/devops_plan.json", response)

    state["devops_plan_path"] = "outputs/devops_plan.json"
    return {
        "devops_plan_path":
        "outputs/devops_plan.json"
    }