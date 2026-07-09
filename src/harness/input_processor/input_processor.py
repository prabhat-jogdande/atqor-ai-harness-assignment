"""
Input Processing Layer

Current:
    Rule Based

Future:
    Azure AI Language
"""

import re


AMBIGUOUS = [
    "sales",
    "revenue",
    "performance",
    "customers",
    "orders"
]


class InputProcessor:

    def sanitize(self, question: str):

        question = question.strip()

        question = re.sub(
            r"\s+",
            " ",
            question
        )

        return question

    def detect_ambiguity(self, question):
        """
        Detect ambiguous business queries.
        """

        q = question.lower().strip()

        # Single-word queries
        if q in AMBIGUOUS:
            return (
                True,
                f"Please clarify what you mean by '{q}'."
            )

        # Very generic business questions
        ambiguous_phrases = [
            "show sales",
            "show revenue",
            "show customers",
            "show orders",
            "show performance",
            "how are we doing"
        ]

        if q in ambiguous_phrases:
            return (
                True,
                "Please provide more details such as time period, region or metric."
            )

        return False, None

    def classify(self, question):

        q = question.lower()

        if "average" in q:
            return "aggregation"

        if "top" in q:
            return "ranking"

        if "trend" in q:
            return "trend"

        if "compare" in q:
            return "comparison"

        return "lookup"


processor = InputProcessor()