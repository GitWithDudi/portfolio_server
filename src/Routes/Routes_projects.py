from flask import Blueprint, request, jsonify

from src.Controller.Controller_projects import get_project_by_id_controller, fach_projects_by_tech,get_all_prijects,attach_project, edit_project, remove_project




projects_bp = Blueprint("projects_routes", __name__)

@projects_bp.route("/projects/tech/<technology>", methods=["GET"])
def fach_projects_by_tech_route(technology):
    return fach_projects_by_tech(technology)


#==================================================================================================

@projects_bp.route("/projects", methods=["GET"])
def get_all_projects_route():
    return get_all_prijects()

#==================================================================================================
@projects_bp.route("/project/<int:project_id>", methods=["GET"])
def get_project_by_id_route(project_id):
    return get_project_by_id_controller(project_id)

#==================================================================================================

@projects_bp.route("/projects", methods=["POST"])
def add_project_route():
    return attach_project()

#==================================================================================================

@projects_bp.route("/project/<int:project_id>", methods=["PUT"])
def update_project_route(project_id):
    return edit_project(project_id)

#==================================================================================================

@projects_bp.route("/project/<int:project_id>", methods=["DELETE"])
def delete_project_route(project_id):
    return remove_project(project_id)