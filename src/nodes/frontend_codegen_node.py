import json

from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter
from src.services.json_loader import JsonLoader

def frontend_codegen_node(state):
    print("=" * 20, "Start frontend_codegen_node")

    prd = JsonLoader.load(state["prd_path"])
    architecture = JsonLoader.load(state["architecture_path"])
    frontend_structure = JsonLoader.load(state["frontend_structure_path"])


    system = PromptLoader.load("agents/frontend_codegen/system.md")
    rules = PromptLoader.load("agents/frontend_codegen/rules.md")
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/frontend_codegen.schema.json")

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

# frontend_structure
{json.dumps(frontend_structure, ensure_ascii=False, indent=2)}

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