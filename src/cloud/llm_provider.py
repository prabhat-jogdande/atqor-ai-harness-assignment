"""
LLM Provider Factory

Current:
    AWS Bedrock

Future:
    Azure OpenAI
"""

import os


def get_provider():

    provider = os.getenv(
        "LLM_PROVIDER",
        "aws"
    ).lower()

    return provider