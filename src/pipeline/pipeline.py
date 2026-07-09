import time

from src.harness.prompt_manager.prompt_builder import build_prompt
from src.harness.orchestrator.llm_client import generate_response
from src.harness.validator.sql_validator import validate_sql
from src.nlp_to_sql.query_executor import execute_query
from src.harness.orchestrator.summarizer import summarize
from src.harness.memory.conversation_memory import memory
from src.harness.input_processor.input_processor import processor
from src.harness.observability.logger import (
    create_trace_id,
    log_request
)
from src.harness.guardrails.guardrails import guardrails


def run_pipeline(
    question,
    session_id="default",
    role="executive"
):

    trace_id = create_trace_id()
    start = time.time()

    # Input processing
    question = processor.sanitize(question)
    intent = processor.classify(question)

    ambiguous, message = processor.detect_ambiguity(question)

    if ambiguous:
        return {
            "success": False,
            "intent": intent,
            "clarification": message
        }

    # Store user message
    memory.add_message(
        session_id,
        "user",
        question
    )

    prompt = build_prompt(question, session_id)

    sql = generate_response(prompt)

    valid, message = validate_sql(sql)

    if not valid:

        latency = round(time.time() - start, 3)

        log_request(
            trace_id,
            question,
            sql,
            False,
            latency
        )

        return {
            "success": False,
            "intent": intent,
            "error": message,
            "trace_id": trace_id
        }

    if not guardrails.check_role(role, sql):

        return {
            "success": False,
            "error": "Access Denied"
        }

    status, result = execute_query(sql)

    if not status:

        latency = round(time.time() - start, 3)

        log_request(
            trace_id,
            question,
            sql,
            False,
            latency
        )

        return {
            "success": False,
            "intent": intent,
            "error": result,
            "trace_id": trace_id
        }

    summary = summarize(question, result)

    # Store assistant response
    memory.add_message(
        session_id,
        "assistant",
        summary
    )

    latency = round(time.time() - start, 3)

    log_request(
        trace_id,
        question,
        sql,
        True,
        latency
    )

    rows = result.to_dict(
        orient="records"
    )

    rows = guardrails.mask_pii(rows)

    return {
        "success": True,
        "intent": intent,
        "trace_id": trace_id,
        "question": question,
        "sql": sql,
        "rows": rows,
        "summary": summary
    }