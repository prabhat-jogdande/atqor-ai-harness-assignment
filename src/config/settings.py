"""
Application Configuration

Current:
    Local Environment Variables

Future:
    Azure Key Vault
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # LLM
    MODEL_ID = os.getenv("MODEL_ID")
    AWS_REGION = os.getenv("AWS_REGION")

    # Database
    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "data/business.db"
    )

    # Prompt
    PROMPT_VERSION = os.getenv(
        "PROMPT_VERSION",
        "v1"
    )

    # Retrieval
    TOP_K = int(
        os.getenv("TOP_K", 3)
    )

    # Debug
    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"


settings = Settings()