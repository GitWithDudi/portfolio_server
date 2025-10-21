from src.Utils.db_config import get_db_connection
import psycopg2.extras
from src.Utils.dict_true import rows_to_dict


def get_all_recommendations():
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM portfolio.recommenders")
        recommendations = cur.fetchall()
        return rows_to_dict(recommendations)
    
#==================================================================================================
    

def add_recommendation(name, role, company,recommendation_file_path=None, recommendation_date=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""INSERT INTO portfolio.recommenders
                    (name, role, company, recommendation_file_path, recommendation_date)
                    VALUES (%s, %s, %s, %s, %s)""",
                    (name, role, company,recommendation_file_path, recommendation_date))
        conn.commit()
        
#==================================================================================================        
        



def delete_reco_and_return_path(rec_id: int) -> str | None:
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            DELETE FROM portfolio.recommenders
            WHERE id = %s
            RETURNING recommendation_file_path;
            """,
            (rec_id,)
        )
        row = cur.fetchone()
        conn.commit()
        return row[0] if row else None

        

