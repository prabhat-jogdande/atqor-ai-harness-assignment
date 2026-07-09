from src.cloud.azure_sql import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("SELECT @@VERSION")

row = cursor.fetchone()

print(row[0])

conn.close()