from flask import request, jsonify, Blueprint
from app import  db,app
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text  # Importa la función text de SQLAlchemy
from flask import render_template
from app.models.user import User  # Importa la clase User del modelo
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
import os

# Crea un Blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__)

# Definición de rutas y vistas


# usando temaplate
@auth_bp.route('/')
def index():
    mensaje = "¡Hola, mundo!"
    return render_template('index.html', mensaje=mensaje)


# Este servicio sirve para validar la conexion con la bd
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


# Vista Register
@auth_bp.route('/register',  methods=['GET'])
def formRegister():
    return render_template('register.html')

# Servicio post register
@auth_bp.route('/register',  methods=['POST'])
def register():

    if request.method == 'POST':
        # Obtiene los datos del formulario de registro
        data = request.form.to_dict()
        foto = request.files.get('foto')  # Obtiene el archivo de imagen cargado

        nombre = data['nombre']
        apellidos = data['apellidos']
        dni = data['dni']
        nick = data['nick']
        password = data['password']

        # Verifica si el usuario ya existe en la base de datos
        existing_user = User.query.filter_by(dni=dni).first()
        if existing_user:
            return jsonify({'message': 'El usuario ya existe'}), 400

        # Si se proporciona una imagen, guárdala en el servidor
        if foto:
            # Verifica si la extensión del archivo es válida (por ejemplo, solo permite imágenes JPEG)
            if not allowed_file_extension(foto.filename):
                return jsonify({'message': 'Tipo de archivo no permitido para la imagen'}), 400

            # Genera un nombre único para la imagen de perfil (puedes usar bibliotecas como uuid)
            unique_filename = generate_unique_filename(foto.filename)

            # Guarda la imagen en un directorio de imágenes de perfil (ajusta la ubicación según tu configuración)
            foto.save(os.path.join(app.config['PROFILE_PICTURES_FOLDER'], unique_filename))

            # Guarda el nombre del archivo en la base de datos para este usuario
            data['foto'] = unique_filename



        # Crea un nuevo usuario y guárdalo en la base de datos
        nuevo_usuario = User(nombre=nombre, apellidos=apellidos, dni=dni, nick=nick, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
 
    return jsonify({'message': 'Nuevo usuario registrado.'}), 200
#@auth_bp.route('/register', methods=['POST'])
#def register():
#    if request.method == 'POST':
#        # Obtén los datos del formulario de registro
#        data = request.form.to_dict()
#        foto = request.files.get('foto')  # Obtiene el archivo de imagen cargado
#
#        # Verifica si el usuario ya existe en la base de datos
#        existing_user = User.query.filter_by(dni=data['dni']).first()
#        if existing_user:
#            return jsonify({'message': 'El usuario ya existe'}), 400
#
#        # Si se proporciona una imagen, guárdala en el servidor
#        if foto:
#            # Verifica si la extensión del archivo es válida (por ejemplo, solo permite imágenes JPEG)
#            if not allowed_file_extension(foto.filename):
#                return jsonify({'message': 'Tipo de archivo no permitido para la imagen'}), 400
#
#            # Genera un nombre único para la imagen de perfil (puedes usar bibliotecas como uuid)
#            unique_filename = generate_unique_filename(foto.filename)
#
#            # Guarda la imagen en un directorio de imágenes de perfil (ajusta la ubicación según tu configuración)
#            foto.save(os.path.join(app.config['PROFILE_PICTURES_FOLDER'], unique_filename))
#
#            # Guarda el nombre del archivo en la base de datos para este usuario
#            data['foto'] = unique_filename
#
#        # Crea un nuevo usuario y guárdalo en la base de datos
#        nuevo_usuario = User(**data)
#        db.session.add(nuevo_usuario)
#        db.session.commit()
#
#    return jsonify({'message': 'Nuevo usuario registrado.'}), 200

# # Función para verificar la extensión de archivo permitida
# def allowed_file_extension(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}
# 
# # Función para generar un nombre de archivo único (puedes ajustar esto según tus necesidades)
# def generate_unique_filename(filename):
#     import uuid
#     unique_filename = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1].lower()
#     return unique_filename
# 
# Vista del formulario Login
@auth_bp.route('/login',  methods=['GET'])
def formLogin():
    return render_template('login.html')






# Servicio post login, si la contrasena es correcta retorna un token que debe guardarse en las cookies
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nick = data.get('nick')
    password = data.get('password')


    print(nick + " " + password)
    # Busca al usuario por su nick en la base de datos
    user = User.query.filter_by(nick=nick).first()
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    print( " ----------------------" )
    print( user.password )
    print( password )
    print( " ----------------------" )
    
    # check_password_hash se utiliza para verificar contraseñas en texto claro con su io
    ## if not check_password_hash(user.password, password):
    if user.password == password :
        return jsonify({'message': 'Contraseña incorrecta'}), 401

    # Genera un token JWT para el usuario
    access_token = create_access_token(identity=user.id)

    return jsonify({'access_token': access_token}), 200



# Función para verificar la extensión de archivo permitida
def allowed_file_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

# Función para generar un nombre de archivo único (puedes ajustar esto según tus necesidades)
def generate_unique_filename(filename):
    import uuid
    unique_filename = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1].lower()
    return unique_filename
