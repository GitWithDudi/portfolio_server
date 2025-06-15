from src.Utils.db_config import get_db_connection
import psycopg2.extras
from src.Utils.dict_true import rows_to_dict



def get_projects():
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
           SELECT 
    p.id,
    p.project_name,
    p.purpose,
    p.github_link,
    p.docker_link,
    p.image_filename,
    ARRAY_AGG(t.name) FILTER (WHERE t.name IS NOT NULL) AS technologies
FROM portfolio.projects p
LEFT JOIN portfolio.project_technologies pt ON p.id = pt.project_id
LEFT JOIN portfolio.technologies t ON pt.technology_id = t.id
GROUP BY 
    p.id, 
    p.project_name, 
    p.purpose, 
    p.github_link, 
    p.docker_link, 
    p.image_filename;

        """)
        projects = cur.fetchall()
        return rows_to_dict(projects)
    
    
def get_project_by_id(project_id):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT 
                p.id,
                p.project_name,
                p.purpose,
                p.github_link,
                p.docker_link,
                p.image_filename,
                ARRAY_AGG(t.name) FILTER (WHERE t.name IS NOT NULL) AS technologies
            FROM portfolio.projects p
            LEFT JOIN portfolio.project_technologies pt ON p.id = pt.project_id
            LEFT JOIN portfolio.technologies t ON pt.technology_id = t.id
            WHERE p.id = %s
            GROUP BY p.id, p.project_name, p.purpose, p.github_link, p.docker_link, p.image_filename
        """, (project_id,))
        project = cur.fetchone()
        if project:
            return dict(project)
        else:
            return None



def get_project_by_technology(technology):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT 
                p.id,
                p.project_name,
                p.purpose,
                p.github_link,
                p.docker_link,
                p.image_filename,
                ARRAY_AGG(t2.name) FILTER (WHERE t2.name IS NOT NULL) AS technologies
            FROM portfolio.projects p
            JOIN portfolio.project_technologies pt1 ON p.id = pt1.project_id
            JOIN portfolio.technologies t1 ON t1.id = pt1.technology_id
            LEFT JOIN portfolio.project_technologies pt2 ON p.id = pt2.project_id
            LEFT JOIN portfolio.technologies t2 ON pt2.technology_id = t2.id
            WHERE t1.name = %s
            GROUP BY p.id, p.project_name, p.purpose, p.github_link, p.docker_link, p.image_filename
        """, (technology,))
        projects = cur.fetchall()
        return rows_to_dict(projects)

    

def add_project (project_name, purpose,  tech_ids, image_filename, github_link=None, docker_link=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute("""INSERT INTO portfolio.projects
                    (project_name, purpose,image_filename, github_link, docker_link  )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id""",
                    (project_name, purpose,image_filename, github_link, docker_link))
        project_id = cur.fetchone()[0]
        
        for tech_id in tech_ids:
                cur.execute("""
                    INSERT INTO portfolio.project_technologies (project_id, technology_id)
                    VALUES (%s, %s)
                """, (project_id, tech_id))

        conn.commit()
        

def update_project (project_id, project_name, purpose, tech_ids, image_filename, github_link=None, docker_link=None):
    with get_db_connection() as conn:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute("""UPDATE portfolio.projects
                    SET project_name = %s,
                        purpose = %s,
                        image_filename = %s,
                        github_link = %s,
                        docker_link = %s
                    WHERE id = %s""",
                    (project_name, purpose, image_filename, github_link, docker_link, project_id))
        
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