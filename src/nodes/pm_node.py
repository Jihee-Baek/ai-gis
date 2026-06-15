from src.services.prompt_loader import PromptLoader
from src.services.gemini_executor import GeminiExecutor
from src.services.output_writer import OutputWriter

def pm_node(state):
    
    print('='*20, 'Start pm_node')

    system = PromptLoader.load("agents/pm/system.md")
    rules = PromptLoader.load("agents/pm/rules.md") 
    language = PromptLoader.load("shared/language_policy.md")
    output_contract = PromptLoader.load("shared/output_contract.md")
    schema = PromptLoader.load("schema/prd.schema.json")

    prompt = f"""
{system}

{rules}

{language}

{output_contract}

# User Request

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