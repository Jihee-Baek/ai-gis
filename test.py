
""" 
# gemini_executor.py 테스트
"""

from src.services.gemini_executor import GeminiExecutor

result = GeminiExecutor.run(
    "대한민국 수도는?"
)

print(result)


""" 
# prompt_loader.py 테스트
"""
"""
from src.services.prompt_loader import PromptLoader

system = PromptLoader.load(
    "agents/pm/system.md"
)

print(system)
"""


