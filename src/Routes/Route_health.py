from src.Controller.Controller_health import health_controller
from flask import Blueprint

health_bp = Blueprint("health_routes", __name__)

@health_bp.route("/health", methods=["GET"])
def health_route():
    return health_controller()