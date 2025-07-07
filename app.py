from src.Routes.Routes_projects import projects_bp
from src.Routes.Routes_tech import technologies_bp
from src.Routes.Routes_reco import reco_bp
from src.Routes.Route_login import login_bp  # שים לב לתיקון שם הקובץ - Route_login → Routes_login
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()  # טוען את משתני הסביבה

app = Flask(__name__)

# חובה להגדיר מפתח סודי ל-JWT מה-env
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

jwt = JWTManager(app)  # מאתחל את JWT עם האפליקציה

CORS(app)

app.register_blueprint(projects_bp)
app.register_blueprint(technologies_bp)
app.register_blueprint(reco_bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
