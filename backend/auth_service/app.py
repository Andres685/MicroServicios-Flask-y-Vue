import os
from flask import Flask
from .models import db
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
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)