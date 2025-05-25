from flask import Blueprint, request, jsonify
from src.Controller.Controller_reco import fetch_all_recommendations, attach_recommendation, remove_reco


reco_bp = Blueprint("reco_routes", __name__)

@reco_bp.route("/recommendations", methods=["GET"])
def get_all_recommendations_route():
    return fetch_all_recommendations()

#==================================================================================================

@reco_bp.route("/recommendations", methods=["POST"])
def add_recommendation_route():
    return attach_recommendation()

#==================================================================================================

@reco_bp.route("/recommendation/<int:reco_id>", methods=["DELETE"])
def delete_recommendation_route(reco_id):
    return remove_reco(reco_id)



