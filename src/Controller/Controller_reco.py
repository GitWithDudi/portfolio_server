from flask import jsonify, request
from werkzeug.utils import secure_filename
import os
import validators
from src.Model.Model_reco import get_all_recommendations, add_recommendation,delete_reco_and_return_path

def fetch_all_recommendations():
    recommendations = get_all_recommendations()
    
    result = []
    for recommendation in recommendations:
        result.append({
            "id": recommendation["id"],
            "name": recommendation["name"],
            "role": recommendation["role"],
            "company": recommendation["company"],
            "recommendation_file_path": recommendation["recommendation_file_path"],
            "recommendation_date": recommendation["recommendation_date"]
        })
    
    return jsonify(result), 200

#==================================================================================================


UPLOAD_FOLDER = os.path.join('src', 'assets', 'documents')
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def attach_recommendation():
    name = request.form.get('name')
    role = request.form.get('role')
    company = request.form.get('company')
    recommendation_date = request.form.get('recommendation_date')

    if not name or not role or not company:
        return jsonify({'error': 'Missing required fields'}), 400

    file = request.files.get('file')

    if not file:
        return jsonify({'error': 'Missing file in request'}), 400

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Only PDF files are allowed'}), 400

    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        add_recommendation(
            name=name,
            role=role,
            company=company,
            recommendation_file_path=file_path,
            recommendation_date=recommendation_date
        )

        return jsonify({'message': 'Recommendation uploaded successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#==================================================================================================


def remove_reco(rec_id):
    if not rec_id:
        return jsonify({"error": "id is required"}), 400

    try:
        file_path = delete_reco_and_return_path(rec_id)

        if file_path and os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({"message": "Recommendation deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
