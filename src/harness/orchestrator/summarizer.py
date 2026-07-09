from src.harness.orchestrator.llm_client import generate_response


def summarize(question, dataframe):

    prompt = f"""
You are a Business Intelligence Analyst.

User Question:
{question}

SQL Result:

{dataframe.to_markdown(index=False)}

Write a professional business summary.

Rules:
- Maximum 3 bullet points.
- Mention important numbers.
- Do not repeat the table.
- Keep the summary concise.
"""

    return generate_response(prompt)