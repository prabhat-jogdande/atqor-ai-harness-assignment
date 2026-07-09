from src.harness.prompt_manager.prompt_builder import build_prompt

question = "Show top 10 customers by revenue"

prompt = build_prompt(question)

print(prompt)