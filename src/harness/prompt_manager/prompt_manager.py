"""
Prompt Version Manager

Current:
    Local Prompt Files

Future:
    Azure Blob Storage
"""

from pathlib import Path


class PromptManager:

    def __init__(self):

        self.prompt_root = Path("prompts")

    def get_latest_version(self):

        latest = self.prompt_root / "latest.txt"

        return latest.read_text().strip()

    def load_prompt(self, version=None):

        if version is None:
            version = self.get_latest_version()

        prompt_file = (
            self.prompt_root /
            version /
            "system_prompt.txt"
        )

        return prompt_file.read_text()