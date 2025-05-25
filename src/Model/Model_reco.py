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

# def get_recommendation_by_id(recommendation_id):
#     with get_db_connection() as conn:
#         cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         cur.execute("SELECT * FROM portfolio.recommenders WHERE id = %s", (recommendation_id,))
#         recommendation = cur.fetchone()
#         return dict(recommendation) if recommendation else None
    
#==================================================================================================    
    

def add_recommendation(name, role, company,recommendation_file_path, recommendation_date=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""INSERT INTO portfolio.recommenders
                    (name, role, company, recommendation_file_path, recommendation_date)
                    VALUES (%s, %s, %s, %s, %s)""",
                    (name, role, company,recommendation_file_path, recommendation_date))
        conn.commit()
        
#==================================================================================================        
        

# def update_recommendation (id, name, role, company, recommendation_file_path, recommendation_date=None):
#     with get_db_connection() as conn:
#         cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
#         cur.execute("""UPDATE portfolio.recommenders
#                     SET name = %s,
#                         role = %s,
#                         company = %s,
#                         recommendation_file_path = %s,
#                         recommendation_date = %s
#                     WHERE id = %s""",
#                     (name, role, company, recommendation_file_path, recommendation_date, id))
#         conn.commit()
        
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

        

