from flask import Flask
from flask_cors import CORS
from .routes import routes
from .config import Config

app = Flask(__name__)

# Cargar configuración
app.config.from_object(Config)

# Habilitar CORS
CORS(app)

# Registrar las rutas
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(port=5001, debug=True)