import sqlite3

conn = sqlite3.connect("data/business.db")
cursor = conn.cursor()

cursor.executescript("""

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS campaign_conversions;
DROP TABLE IF EXISTS support_tickets;

CREATE TABLE customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    segment TEXT,
    region TEXT,
    created_at DATE
);

CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    sub_category TEXT,
    brand TEXT,
    cost_price REAL,
    list_price REAL
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    status TEXT,
    total_amount REAL,
    discount REAL,
    channel TEXT
);

CREATE TABLE order_items(
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    line_total REAL
);

CREATE TABLE campaigns(
    id INTEGER PRIMARY KEY,
    name TEXT,
    channel TEXT,
    start_date DATE,
    end_date DATE,
    budget REAL,
    spend REAL
);

CREATE TABLE campaign_conversions(
    id INTEGER PRIMARY KEY,
    campaign_id INTEGER,
    customer_id INTEGER,
    order_id INTEGER,
    conversion_date DATE
);

CREATE TABLE support_tickets(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_id INTEGER,
    category TEXT,
    priority TEXT,
    status TEXT,
    created_at DATE,
    resolved_at DATE
);

""")

conn.commit()
conn.close()

print("Database Created Successfully")