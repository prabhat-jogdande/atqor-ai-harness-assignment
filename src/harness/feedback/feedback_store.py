"""
Feedback Store

Current:
    Local JSON

Future:
    Azure Blob Storage / Cosmos DB
"""

import json
from pathlib import Path


FEEDBACK_FILE = Path("data/feedback/feedback.json")


def save_feedback(
    session_id,
    question,
    sql,
    summary,
    rating,
    corrected_sql=None
):
    """
    Save user feedback.
    """

    with open(FEEDBACK_FILE, "r") as f:
        data = json.load(f)

    data.append({
        "session_id": session_id,
        "question": question,
        "generated_sql": sql,
        "summary": summary,
        "rating": rating,
        "corrected_sql": corrected_sql
    })

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return True