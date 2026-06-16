import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader

def backend_codegen_node(state):
    print("=" * 20, "Start backend_codegen_node")

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])
    backend_structure = JsonLoader.load(state["backend_structure_path"])


    system = PromptLoader.load("agents/backend_codegen/system.md")
    rules = PromptLoader.load("agents/backend_codegen/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/backend_codegen.schema.json")

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

# Backend_structure
{json.dumps(backend_structure, ensure_ascii=False, indent=2)}

# Output Schema
{schema}

Output must follow backend codegen exactly.
Return JSON only.

Generate:
outputs/backend_codegen.json
"""

    response = GeminiExecutor.run(prompt)

    OutputWriter.save_json("outputs/backend_codegen.json", response)

    state["backend_codegen_path"] = "outputs/backend_codegen.json"

    return {
        "backend_codegen_path":
        "outputs/backend_codegen.json"
    }