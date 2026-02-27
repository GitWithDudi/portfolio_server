from src.Utils.db_config import get_db_connection

def health_check():
     with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM portfolio.health LIMIT 1")
        result = cur.fetchone()
        return result