from flask import Flask

app = Flask(__name__)

# Configuración de la aplicación (opcional)
# app.config['SECRET_KEY'] = 'tu_clave_secreta'

from app import routes