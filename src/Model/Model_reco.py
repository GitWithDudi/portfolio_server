from Utils.db_config import get_db_connection
import psycopg2.extras
from Utils.dict_true import rows_to_dict


def get_all_recommendations():
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM recommenders")
        recommendations = cur.fetchall()
        return rows_to_dict(recommendations)
    

def add_recommendation(name, role, company,recommendation_file_path, recommendation_date=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""INSERT INTO recommenders
                    (name, role, company, recommendation_file_path, recommendation_date)
                    VALUES (%s, %s, %s, %s, %s)""",
                    (name, role, company,recommendation_file_path, recommendation_date))
        conn.commit()
        

def update_recommendation (id, name, role, company, recommendation_file_path, recommendation_date=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute("""UPDATE recommenders
                    SET name = %s,
                        role = %s,
                        company = %s,
                        recommendation_file_path = %s,
                        recommendation_date = %s
                    WHERE id = %s""",
                    (name, role, company, recommendation_file_path, recommendation_date, id))
        conn.commit()
        


def delete_recommendation(id):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute("""DELETE FROM recommenders WHERE id = %s""", (id,))
        conn.commit()
        

