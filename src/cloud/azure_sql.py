import pyodbc

from src.config.settings import settings

_connection = None


def get_connection():

    global _connection

    if _connection is None:

        _connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={settings.AZURE_SQL_SERVER};"
            f"DATABASE={settings.AZURE_SQL_DATABASE};"
            f"UID={settings.AZURE_SQL_USERNAME};"
            f"PWD={settings.AZURE_SQL_PASSWORD};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )

    return _connection