from src.Model.Model_projects import  get_project_by_technology, get_projects, add_project, update_project, delete_project
from flask import jsonify, request
import validators


def fach_projects_by_tech(technology):
    projects = get_project_by_technology(technology)
    
    if not technology:
        return jsonify({"error": "most be select technology"}), 404
    
    
    
    result = []
    for project in projects:
        result.append({
            "id": project["id"],
            "project_name": project["project_name"],
            "purpose": project["purpose"],
            "github_link": project["github_link"],
            "docker_link": project["docker_link"]
        })
    
    return jsonify(result), 200


#==================================================================================================

def get_all_prijects():
    projects = get_projects()
    
    result = []
    for project in projects:
        result.append({
            "id": project["id"],
            "project_name": project["project_name"],
            "purpose": project["purpose"],
            "image_filename": project["image_filename"],
            "github_link": project["github_link"],
            "docker_link": project["docker_link"]
        })
    
    return jsonify(result), 200

#==================================================================================================
#project_name, purpose,  tech_ids, github_link=None, docker_link=None


def attach_project():
    data = request.get_json()
    
    project_name = data.get("project_name")
    purpose = data.get("purpose")
    tech_ids = data.get("tech_ids", [])
    image_filename = data.get("image_filename")
    github_link = data.get("github_link")
    docker_link = data.get("docker_link")
    
    
    if not project_name or not purpose or not tech_ids:
        return jsonify({"error": "project_name, purpose and tech_ids are required"}), 400
    
    if not github_link or not validators.url(github_link):
        return jsonify({"error": "Invalid GitHub link"}), 400
    
    if docker_link and not validators.url(docker_link):
        return jsonify({"error": "Invalid Docker link"}), 400
    
    try:
        add_project(project_name, purpose, tech_ids, image_filename, github_link, docker_link)
        return jsonify({"message": "Project added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
#==================================================================================================

def edit_project(project_id):
    data = request.get_json()
    
    project_id = data.get("project_id")
    project_name = data.get("project_name")
    purpose = data.get("purpose")
    tech_ids = data.get("tech_ids", [])
    image_filename = data.get("image_filename")
    github_link = data.get("github_link")
    docker_link = data.get("docker_link")
    
    
    if not project_id or not project_name or not purpose or not tech_ids:
        return jsonify({"error": "project_id, project_name, purpose and tech_ids are required"}), 400
    
    if github_link and not validators.url(github_link):
        return jsonify({"error": "Invalid GitHub link"}), 400
    
    if docker_link and not validators.url(docker_link):
        return jsonify({"error": "Invalid Docker link"}), 400
    
    try:
        update_project(project_id, project_name, purpose, tech_ids, image_filename, github_link, docker_link)
        return jsonify({"message": "Project updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
#==================================================================================================

def remove_project(project_id):
    if not project_id:
        return jsonify({"error": "project_id is required"}), 400
    
    try:
        delete_project(project_id)
        return jsonify({"message": "Project deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    
    
