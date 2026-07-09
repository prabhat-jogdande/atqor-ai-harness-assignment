from src.harness.validator.sql_validator import validate_sql

sql = """
DROP TABLE customers;
"""

valid, message = validate_sql(sql)

print(valid)
print(message)