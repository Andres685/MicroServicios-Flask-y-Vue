from flask import Flask
from .models import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .routes import routes
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)
CORS(app)
db.init_app(app)

app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5000, debug=True)