from flask import Flask
from .models import db
from .routes import routes
from .config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Cargar configuración
app.config.from_object(Config)

# Inicializar base de datos
db.init_app(app)

# Registrar rutas
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)