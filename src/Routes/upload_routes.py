from flask import Blueprint
from src.Controller.upload_controller import upload_file

upload_bp = Blueprint('upload_bp', __name__)

upload_bp.route('/upload', methods=['POST'])(upload_file)
