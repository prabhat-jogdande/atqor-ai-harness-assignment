import sqlite3
import pandas as pd

from src.config.settings import settings
from src.cloud.azure_sql import get_connection


DB_PATH = settings.DATABASE_PATH


def execute_query(sql):

    # Azure SQL
    if settings.DATABASE_PROVIDER == "azure":

        conn = get_connection()

    # Local SQLite
    else:

        conn = sqlite3.connect(DB_PATH)

    try:

        df = pd.read_sql_query(
            sql,
            conn
        )

        return True, df

    except Exception as e:

        return False, str(e)


    finally:
        pass
        # conn.close()