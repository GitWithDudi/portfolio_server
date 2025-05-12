from Utils.db_config import get_db_connection
import psycopg2.extras
from Utils.dict_true import rows_to_dict



def get_all_technologies():
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM technologies")
        technologies = cur.fetchall()
        return rows_to_dict(technologies)
