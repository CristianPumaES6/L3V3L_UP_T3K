from flask import request, jsonify, Blueprint
from app import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text  # Importa la función text de SQLAlchemy
from flask import render_template


# Crea un Blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__)

# usando temaplate
@auth_bp.route('/')
def index():
    mensaje = "¡Hola, mundo!"
    return render_template('index.html', mensaje=mensaje)



# Definición de rutas y vistas
@auth_bp.route('/test_db_connection', methods=['GET'])
def test_db_connection():
    try:
         # Declara la consulta SQL como un objeto text
        query = text('SELECT 1')
        
        # Ejecuta la consulta
        db.session.execute(query)

        return 'Conexión a la base de datos exitosa'
    except SQLAlchemyError as e:
        return 'Error de conexión a la base de datos: ' + str(e), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    # Lógica para el registro de usuarios
    # ...
    return jsonify({'access_token': access_token}), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    # Lógica para la autenticación de usuarios
    # ...
    return jsonify({'access_token': access_token}), 200

