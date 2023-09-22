from flask import request, jsonify, Blueprint
from app import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text  # Importa la función text de SQLAlchemy
from flask import render_template
from app.models.user import User  # Importa la clase User del modelo


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



@auth_bp.route('/register',  methods=['GET'])
def formRegister():
    return render_template('register.html')


@auth_bp.route('/register',  methods=['POST'])
def register():

    if request.method == 'POST':
        # Obtiene los datos del formulario de registro
        data = request.get_json()
        nombre = data.get('nombre')
        apellidos = data.get('apellidos')
        dni = data.get('dni')
        nick = data.get('nick')
        password = data.get('password')

        # Verifica si el usuario ya existe en la base de datos
        existing_user = User.query.filter_by(dni=dni).first()
        if existing_user:
            return jsonify({'message': 'El usuario ya existe'}), 400

        # Crea un nuevo usuario y guárdalo en la base de datos
        nuevo_usuario = User(nombre=nombre, apellidos=apellidos, dni=dni, nick=nick, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
 
    return jsonify({'data': true}), 200


@auth_bp.route('/login', methods=['POST'])
def login():
    # Lógica para la autenticación de usuarios
    # ...
    return jsonify({'access_token': access_token}), 200

