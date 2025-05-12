from src.Routes.Routes_projects import projects_bp
from flask import Flask, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.register_blueprint(projects_bp)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
