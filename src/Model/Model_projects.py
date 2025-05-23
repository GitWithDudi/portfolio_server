from src.Utils.db_config import get_db_connection
import psycopg2.extras
from src.Utils.dict_true import rows_to_dict



def get_projects():
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM portfolio.projects")
        projects = cur.fetchall()
        return rows_to_dict(projects)
    

def get_project_by_technology(technology):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""SELECT p.*
                       FROM portfolio.projects p
                       JOIN project_technologies pt ON p.id = pt.project_id
                       JOIN technologies t ON t.id = pt.technology_id
                       WHERE t.name = %s""" , (technology,))
        projects = cur.fetchall()
        return rows_to_dict(projects)
    

def add_project (project_name, purpose,  tech_ids, github_link=None, docker_link=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute("""INSERT INTO portfolio.projects
                    (project_name, purpose, github_link, docker_link  )
                    VALUES (%s, %s, %s, %s)
                    RETURNING id""",
                    (project_name, purpose, github_link, docker_link))
        project_id = cur.fetchone()[0]
        
        for tech_id in tech_ids:
                cur.execute("""
                    INSERT INTO portfolio.project_technologies (project_id, technology_id)
                    VALUES (%s, %s)
                """, (project_id, tech_id))

        conn.commit()
        

def update_project (project_id, project_name, purpose, tech_ids, github_link=None, docker_link=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute("""UPDATE portfolio.projects
                    SET project_name = %s,
                        purpose = %s,
                        github_link = %s,
                        docker_link = %s
                    WHERE id = %s""",
                    (project_name, purpose, github_link, docker_link, project_id))
        
        cur.execute("""DELETE FROM portfolio.project_technologies WHERE project_id = %s""", (project_id,))

        for tech_id in tech_ids:
            cur.execute("""INSERT INTO portfolio.project_technologies (project_id, technology_id)
                        VALUES (%s, %s)""",
                        (project_id, tech_id))

        conn.commit()

def delete_project (project_id):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute("""DELETE FROM portfolio.projects WHERE id = %s""", (project_id,))
        conn.commit()