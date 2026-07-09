"""
Guardrails

Current:
    Local Role Configuration

Future:
    Azure Identity + Azure AI Language
"""

import json
import re


with open("src/harness/guardrails/roles.json") as f:
    ROLES = json.load(f)


class GuardRails:

    def check_role(self, role, sql):

        allowed = ROLES.get(role)

        if allowed is None:
            return False

        tables = allowed["tables"]

        found = re.findall(
            r"(?:FROM|JOIN)\s+([a-zA-Z_]+)",
            sql,
            re.IGNORECASE
        )

        for table in found:

            if table not in tables:
                return False

        return True

    def mask_pii(self, rows):

        for row in rows:

            if "email" in row:

                row["email"] = "*****"

        return rows


guardrails = GuardRails()