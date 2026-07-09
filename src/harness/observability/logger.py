"""
Logging Module

Current:
    Local File Logging

Future:
    Azure Application Insights
"""

import logging
import uuid


logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


logger = logging.getLogger("nl2sql")


def create_trace_id():
    """
    Create unique trace id.
    """
    return str(uuid.uuid4())


def log_request(
    trace_id,
    question,
    sql,
    success,
    latency
):
    """
    Log pipeline execution.
    """

    logger.info(
        {
            "trace_id": trace_id,
            "question": question,
            "sql": sql,
            "success": success,
            "latency": latency
        }
    )