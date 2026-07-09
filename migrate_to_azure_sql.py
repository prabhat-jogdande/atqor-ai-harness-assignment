import sqlite3
from src.cloud.azure_sql import get_connection

sqlite_conn = sqlite3.connect("data/business.db")
sqlite_cur = sqlite_conn.cursor()

azure_conn = get_connection()
azure_cur = azure_conn.cursor()

# Disable fast_executemany (safer if you saw MemoryError)
azure_cur.fast_executemany = False

tables = [
    "customers",
    "products",
    "orders",
    "order_items",
    "campaigns",
    "campaign_conversions",
    "support_tickets"
]

# Delete existing data (child tables first)
print("Clearing existing Azure SQL data...")

delete_order = [
    "campaign_conversions",
    "support_tickets",
    "order_items",
    "orders",
    "campaigns",
    "products",
    "customers"
]

for table in delete_order:
    try:
        azure_cur.execute(f"DELETE FROM {table}")
        azure_conn.commit()
        print(f"Cleared {table}")
    except Exception as e:
        print(f"Could not clear {table}: {e}")

print("\nStarting migration...\n")

BATCH_SIZE = 500

for table in tables:

    print(f"Migrating {table}...")

    sqlite_cur.execute(f"SELECT * FROM {table}")

    total = 0

    while True:

        rows = sqlite_cur.fetchmany(BATCH_SIZE)

        if not rows:
            break

        placeholders = ",".join(["?"] * len(rows[0]))

        azure_cur.executemany(
            f"INSERT INTO {table} VALUES ({placeholders})",
            rows
        )

        azure_conn.commit()

        total += len(rows)

        print(f"Inserted {total} rows into {table}")

print("\nMigration Completed Successfully!")

sqlite_conn.close()
azure_conn.close()