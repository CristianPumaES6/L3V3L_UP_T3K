from flask import Blueprint
# from flask import render_template

# Crea un Blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__)
from app.routes.auth import *
#from app import app


# Crea un objeto Blueprint para las rutas de imágenes
images_bp = Blueprint('images', __name__)
from app.routes.images import *