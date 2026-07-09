import os
import json
import boto3
from dotenv import load_dotenv

from src.config.settings import settings
from src.cloud.llm_provider import get_provider
from src.cloud.azure_openai import generate_response as azure_generate_response

load_dotenv()

DEBUG = settings.DEBUG

client = boto3.client(
    "bedrock-runtime",
    region_name=settings.AWS_REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

# MODEL_ID = os.getenv("MODEL_ID")
MODEL_ID = settings.MODEL_ID


def generate_response(prompt: str) -> str:
    """
    Send prompt to the configured LLM and return plain text response.

    Supports:
        - Azure OpenAI
        - Amazon Nova
        - Anthropic Claude
    """

    provider = get_provider()

    # Azure
    if provider == "azure":
        return azure_generate_response(prompt)

    # AWS
    if provider != "aws":
        raise ValueError(f"Unsupported provider: {provider}")

    if DEBUG:
        print(f"MODEL_ID: {MODEL_ID}")

    # Amazon Nova
    if MODEL_ID.startswith("amazon.nova"):

        body = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 1024,
                "temperature": 0
            }
        }

    # Claude
    elif MODEL_ID.startswith("anthropic."):

        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "temperature": 0,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

    else:
        raise ValueError(f"Unsupported model: {MODEL_ID}")

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())

    if DEBUG:
        print("\n===== RAW RESPONSE =====")
        print(json.dumps(result, indent=2))
        print("========================\n")

    # Extract response text
    if MODEL_ID.startswith("amazon.nova"):

        response_text = result["output"]["message"]["content"][0]["text"]

    elif MODEL_ID.startswith("anthropic."):

        response_text = result["content"][0]["text"]

    else:
        raise ValueError(f"Unsupported model: {MODEL_ID}")

    # Remove markdown if model returns it
    response_text = (
        response_text
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    return response_text