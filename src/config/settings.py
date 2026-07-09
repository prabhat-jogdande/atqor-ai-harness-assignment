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

    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

    AZURE_OPENAI_API_VERSION = os.getenv(
        "AZURE_OPENAI_API_VERSION",
        "v1"
    )

    AZURE_OPENAI_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_DEPLOYMENT",
        "gpt-5"
    )

    AZURE_BLOB_CONNECTION_STRING = os.getenv(
        "AZURE_BLOB_CONNECTION_STRING"
    )

    AZURE_BLOB_CONTAINER = os.getenv(
        "AZURE_BLOB_CONTAINER",
        "ai-harness"
    )

    DATABASE_PROVIDER = os.getenv(
        "DATABASE_PROVIDER",
        "sqlite"
    )

    AZURE_SQL_SERVER = os.getenv(
        "AZURE_SQL_SERVER"
    )

    AZURE_SQL_DATABASE = os.getenv(
        "AZURE_SQL_DATABASE"
    )

    AZURE_SQL_USERNAME = os.getenv(
        "AZURE_SQL_USERNAME"
    )

    AZURE_SQL_PASSWORD = os.getenv(
        "AZURE_SQL_PASSWORD"
    )

settings = Settings()