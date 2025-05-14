from src.Utils.db_config import get_db_connection
import psycopg2.extras
from src.Utils.dict_true import rows_to_dict



def get_all_technologies():
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM portfolio.technologies")
        technologies = cur.fetchall()
        return rows_to_dict(technologies)
    
#================================================================================================== 

def get_technology_by_id(technology_id):    
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM portfolio.technologies WHERE id = %s", (technology_id,))
        technology = cur.fetchone()
        return dict(technology) if technology else None

    
#==================================================================================================    

def add_technology(name):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""INSERT INTO portfolio.technologies (name) VALUES (%s) RETURNING id""", (name,))
        technology_id = cur.fetchone()[0]
        conn.commit()
        return technology_id

#==================================================================================================

def update_technology(id, name):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""UPDATE portfolio.technologies SET name = %s WHERE id = %s""", (name, id))
        conn.commit()
#        return id

#==================================================================================================
def delete_technology(id):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""DELETE FROM portfolio.technologies WHERE id = %s""", (id,))
        conn.commit()
#       return id