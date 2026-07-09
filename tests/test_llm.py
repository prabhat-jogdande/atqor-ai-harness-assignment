from src.harness.prompt_manager.prompt_builder import build_prompt
from src.harness.orchestrator.llm_client import generate_sql

question = "Show top 5 customers by revenue"

prompt = build_prompt(question)

sql = generate_sql(prompt)

print(sql)