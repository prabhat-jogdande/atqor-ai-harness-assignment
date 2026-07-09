from src.harness.prompt_manager.prompt_builder import build_prompt
from src.harness.orchestrator.llm_client import generate_response
from src.harness.validator.sql_validator import validate_sql
from src.nlp_to_sql.query_executor import execute_query

question = input("Ask Question: ")

prompt = build_prompt(question)

sql = generate_response(prompt)

print("\nGenerated SQL:\n")
print(sql)

valid, message = validate_sql(sql)

print("\nValidation:")
print(message)

if not valid:
    exit()

status, result = execute_query(sql)

if status:

    print("\nResult:\n")
    print(result)

else:

    print(result)


from src.harness.orchestrator.summarizer import summarize
summary = summarize(question, result)

print("\nSummary:\n")
print(summary)