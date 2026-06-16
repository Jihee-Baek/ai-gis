import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader

def backend_structure_node(state):
    print("=" * 20, "Start backend_structure_node")

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])
    backend_design = JsonLoader.load(state["backend_design_path"])


    system = PromptLoader.load("agents/backend_structure/system.md")
    rules = PromptLoader.load("agents/backend_structure/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/backend_structure.schema.json")

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

# Backend_design
{json.dumps(backend_design, ensure_ascii=False, indent=2)}

# Output Schema
{schema}

Output must follow backend structure exactly.
Return JSON only.

Generate:
outputs/backend_structure.json
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/backend_structure.json", response)

    state["backend_structure_path"] = "outputs/backend_structure.json"

    return {
        "backend_structure_path":
        "outputs/backend_structure.json"
    }