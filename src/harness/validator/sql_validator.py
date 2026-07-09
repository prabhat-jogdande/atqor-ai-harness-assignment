import re
import sqlglot

ALLOWED_TABLES = {
    "customers",
    "orders",
    "order_items",
    "products",
    "campaigns",
    "campaign_conversions",
    "support_tickets",
}

BLOCKED = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "CREATE",
    "TRUNCATE",
]


def validate_sql(sql: str):

    sql = sql.strip()

    upper = sql.upper()

    for keyword in BLOCKED:
        if keyword in upper:
            return False, f"Blocked keyword: {keyword}"

    if not upper.startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    try:
        sqlglot.parse_one(sql)
    except Exception as e:
        return False, str(e)

    tables = set(
        re.findall(
            r"(?:FROM|JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*)",
            sql,
            re.IGNORECASE,
        )
    )

    for table in tables:
        if table not in ALLOWED_TABLES:
            return False, f"Unknown table: {table}"

    return True, "Valid SQL"

