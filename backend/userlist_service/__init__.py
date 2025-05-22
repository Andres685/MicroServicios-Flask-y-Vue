from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import routes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    # Crear tablas al arrancar
    with app.app_context():
        db.create_all()

    app.register_blueprint(routes)
    return app
