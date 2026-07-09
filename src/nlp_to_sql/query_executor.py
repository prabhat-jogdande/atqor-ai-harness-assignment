import sqlite3
import pandas as pd

from src.config.settings import settings

DB_PATH = settings.DATABASE_PATH


def execute_query(sql):

    conn = sqlite3.connect(DB_PATH)

    try:
        df = pd.read_sql_query(sql, conn)
        return True, df

    except Exception as e:
        return False, str(e)

    finally:
        conn.close()