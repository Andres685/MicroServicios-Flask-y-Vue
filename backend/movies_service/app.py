from flask import Flask
from routes import routes
from config import Config

app = Flask(__name__)

# Cargar configuración
app.config.from_object(Config)

# Registrar rutas
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)