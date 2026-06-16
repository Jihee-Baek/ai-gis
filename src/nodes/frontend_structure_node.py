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

    prompt = f"""
{system}

{rules}

{language}

{output_contract}

Read the following files:

# PRD
{json.dumps(prd, ensure_ascii=False, indent=2)}

# Architecture
{json.dumps(architecture, ensure_ascii=False, indent=2)}

# Frontend_design
{json.dumps(frontend_design, ensure_ascii=False, indent=2)}

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