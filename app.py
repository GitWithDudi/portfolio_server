from src.Routes.Routes_projects import projects_bp
from src.Routes.Routes_tech import technologies_bp
from src.Routes.Routes_reco import reco_bp
from src.Routes.Route_login import login_bp
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

jwt = JWTManager(app)

CORS(app, resources={r"/*": {"origins": [
    "http://localhost:5173",
    "https://davidev.app",
    "https://www.davidev.app"
]}})

app.register_blueprint(projects_bp)
app.register_blueprint(technologies_bp)
app.register_blueprint(reco_bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
