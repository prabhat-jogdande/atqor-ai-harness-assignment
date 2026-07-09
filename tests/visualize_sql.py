import sqlite3
import pandas as pd
import webbrowser
from pathlib import Path

conn = sqlite3.connect("data/business.db")

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)["name"].tolist()

html = """
<html>
<head>
<title>Business Database</title>
<style>
body{
    font-family:Arial;
    margin:40px;
    background:#f5f5f5;
}
h1{
    text-align:center;
}
h2{
    margin-top:40px;
}
table{
    border-collapse:collapse;
    width:100%;
    margin-bottom:30px;
    background:white;
}
th,td{
    border:1px solid #ddd;
    padding:8px;
    text-align:left;
}
th{
    background:#4CAF50;
    color:white;
}
tr:nth-child(even){
    background:#f2f2f2;
}
</style>
</head>
<body>

<h1>Business Database</h1>
"""

for table in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)

    html += f"<h2>{table} ({len(df)} rows)</h2>"
    html += df.to_html(index=False)

html += "</body></html>"

conn.close()

output = Path("database_view.html")
output.write_text(html, encoding="utf-8")

webbrowser.open(output.resolve().as_uri())

print("Database visualization saved to database_view.html")