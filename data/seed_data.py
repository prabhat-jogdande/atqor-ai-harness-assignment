import sqlite3
import random
from faker import Faker
from datetime import timedelta

fake = Faker()

conn = sqlite3.connect("data/business.db")
cursor = conn.cursor()

# -----------------------------------
# Clear Existing Data
# -----------------------------------
tables = [
    "order_items",
    "campaign_conversions",
    "support_tickets",
    "orders",
    "campaigns",
    "products",
    "customers"
]

for table in tables:
    cursor.execute(f"DELETE FROM {table}")

conn.commit()

# -----------------------------------
# Dummy Values
# -----------------------------------
segments = ["Retail", "Enterprise", "SMB"]
regions = ["North", "South", "East", "West"]

order_status = ["Completed", "Pending", "Cancelled"]
channels = ["Online", "Store", "Mobile"]

categories = ["Electronics", "Fashion", "Home", "Sports"]
sub_categories = ["Premium", "Standard", "Budget"]
brands = ["Apple", "Samsung", "Nike", "Sony", "Adidas", "LG"]

ticket_categories = ["Payment", "Delivery", "Refund", "Product"]
priorities = ["Low", "Medium", "High"]
ticket_status = ["Open", "In Progress", "Resolved", "Closed"]

campaign_channels = ["Google", "Facebook", "Email", "Instagram"]

# -----------------------------------
# Customers
# -----------------------------------
for i in range(1, 501):
    cursor.execute(
        """
        INSERT INTO customers
        VALUES (?,?,?,?,?,?)
        """,
        (
            i,
            fake.name(),
            fake.email(),
            random.choice(segments),
            random.choice(regions),
            fake.date_between("-3y", "today"),
        ),
    )

# -----------------------------------
# Products
# -----------------------------------
for i in range(1, 101):

    cost = random.randint(100, 5000)
    price = cost + random.randint(100, 2000)

    cursor.execute(
        """
        INSERT INTO products
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            i,
            fake.word().title(),
            random.choice(categories),
            random.choice(sub_categories),
            random.choice(brands),
            cost,
            price,
        ),
    )

# -----------------------------------
# Orders
# -----------------------------------
for i in range(1, 1001):

    total = random.randint(500, 20000)
    discount = random.randint(0, 25)

    cursor.execute(
        """
        INSERT INTO orders
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            i,
            random.randint(1, 500),
            fake.date_between("-2y", "today"),
            random.choice(order_status),
            total,
            discount,
            random.choice(channels),
        ),
    )

# -----------------------------------
# Order Items
# -----------------------------------
for i in range(1, 2001):

    qty = random.randint(1, 5)
    unit_price = random.randint(100, 3000)

    cursor.execute(
        """
        INSERT INTO order_items
        VALUES (?,?,?,?,?,?)
        """,
        (
            i,
            random.randint(1, 1000),
            random.randint(1, 100),
            qty,
            unit_price,
            qty * unit_price,
        ),
    )

# -----------------------------------
# Campaigns
# -----------------------------------
for i in range(1, 31):

    start = fake.date_between("-1y", "today")
    budget = random.randint(10000, 500000)
    spend = random.randint(int(budget * 0.5), budget)

    cursor.execute(
        """
        INSERT INTO campaigns
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            i,
            fake.word().title(),
            random.choice(campaign_channels),
            start,
            start + timedelta(days=30),
            budget,
            spend,
        ),
    )

# -----------------------------------
# Campaign Conversions
# -----------------------------------
for i in range(1, 501):

    cursor.execute(
        """
        INSERT INTO campaign_conversions
        VALUES (?,?,?,?,?)
        """,
        (
            i,
            random.randint(1, 30),
            random.randint(1, 500),
            random.randint(1, 1000),
            fake.date_between("-1y", "today"),
        ),
    )

# -----------------------------------
# Support Tickets
# -----------------------------------
for i in range(1, 1001):

    created_at = fake.date_between("-1y", "today")

    if random.random() < 0.7:
        resolved_at = created_at + timedelta(days=random.randint(1, 15))
        status = "Resolved"
    else:
        resolved_at = None
        status = random.choice(["Open", "In Progress"])

    cursor.execute(
        """
        INSERT INTO support_tickets
        VALUES (?,?,?,?,?,?,?,?)
        """,
        (
            i,
            random.randint(1, 500),      # customer_id
            random.randint(1, 1000),     # order_id
            random.choice(ticket_categories),
            random.choice(priorities),
            status,
            created_at,
            resolved_at,
        ),
    )

# -----------------------------------
# Commit
# -----------------------------------
conn.commit()
conn.close()

print("✅ Dummy data inserted successfully.")