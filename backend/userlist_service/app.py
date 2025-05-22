from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import routes
from .config import Config
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configuración de extensiones
    CORS(app)
    db.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(routes)
    
    # Crear tablas en la base de datos
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5002, debug=True)