from flask import request, jsonify
from werkzeug.utils import secure_filename
from src.Utils.r2_client import s3_client, R2_BUCKET_NAME, R2_ENDPOINT

def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)

    try:
        s3_client.upload_fileobj(file, R2_BUCKET_NAME, filename)
        file_url = f"{R2_ENDPOINT}/{R2_BUCKET_NAME}/{filename}"
        return jsonify({"url": file_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
