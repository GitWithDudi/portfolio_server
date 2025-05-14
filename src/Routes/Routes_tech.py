from flask import Blueprint, request, jsonify
from src.Controller.Controller_tech import fetch_all_technologies, attach_technology, edit_technology, remove_technology, fetch_technology_by_id


technologies_bp = Blueprint("technologies_routes", __name__)

@technologies_bp.route("/technologies", methods=["GET"])
def get_all_technologies_route():
    return fetch_all_technologies()

#==================================================================================================

@technologies_bp.route("/technologies/<int:technology_id>", methods=["GET"])
def get_technology_by_id_route(technology_id):
    return fetch_technology_by_id(technology_id)

#==================================================================================================

@technologies_bp.route("/technologies", methods=["POST"])
def add_technology_route():
    return attach_technology()

#==================================================================================================

@technologies_bp.route("/technologies/<int:technology_id>", methods=["PUT"])
def update_technology_route(technology_id):
    return edit_technology(technology_id)

#==================================================================================================

@technologies_bp.route("/technologies/<int:technology_id>", methods=["DELETE"])
def delete_technology_route(technology_id):
    return remove_technology(technology_id)