"""
LLM Provider Factory

Current:
    AWS Bedrock

Future:
    Azure OpenAI
"""

import os


def get_provider() -> str:
    """
    Returns the configured LLM provider.

    Supported:
    - aws
    - azure
    """

    return os.getenv(
        "LLM_PROVIDER",
        "aws"
    ).strip().lower()


def is_aws() -> bool:
    return get_provider() == "aws"


def is_azure() -> bool:
    return get_provider() == "azure"