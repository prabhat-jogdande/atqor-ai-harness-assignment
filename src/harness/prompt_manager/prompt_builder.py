import json
from pathlib import Path

from src.harness.retriever.example_retriever import ExampleRetriever
from src.harness.memory.conversation_memory import memory
from src.config.settings import settings
from src.harness.prompt_manager.prompt_manager import PromptManager

# Base Paths
BASE = Path(__file__).resolve().parents[2]

SCHEMA = BASE / "schema" / "schema_metadata.json"
REL = BASE / "schema" / "relationships.json"
DICT = BASE / "schema" / "business_dictionary.json"

# Prompt Manager
prompt_manager = PromptManager()

# Load Schema Metadata
with open(SCHEMA, "r") as f:
    SCHEMA_JSON = json.load(f)

with open(REL, "r") as f:
    REL_JSON = json.load(f)

with open(DICT, "r") as f:
    DICT_JSON = json.load(f)


def build_prompt(user_query: str, session_id="default") -> str:
    """
    Build the final prompt for the LLM.
    """

    # Load latest system prompt
    system_prompt = prompt_manager.load_prompt()

    # Retrieve only the most relevant example
    retriever = ExampleRetriever()
    examples = retriever.retrieve(
        user_query,
        top_k=settings.TOP_K
    )

    # Conversation history
    history = memory.get_history(session_id)

    conversation = ""

    for item in history:
        conversation += f"""
{item['role']}:
{item['content']}
"""

    few_shot_text = ""

    for example in examples:
        few_shot_text += f"""
Question:
{example["question"]}

SQL:
{example["sql"]}

"""

    prompt = f"""
{system_prompt}

==================================================
DATABASE SCHEMA
==================================================

{json.dumps(SCHEMA_JSON, indent=2)}

==================================================
TABLE RELATIONSHIPS
==================================================

{json.dumps(REL_JSON, indent=2)}

==================================================
BUSINESS DICTIONARY
==================================================

{json.dumps(DICT_JSON, indent=2)}

==================================================
FEW SHOT EXAMPLES
==================================================

{few_shot_text}

==================================================
CONVERSATION HISTORY
==================================================

{conversation}

==================================================
USER QUESTION
==================================================

{user_query}

==================================================
RETURN ONLY SQL
==================================================
"""

    return prompt