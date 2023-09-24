from flask import request, jsonify, send_file
from app.routes import images_bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import  db,app
from flask import render_template
from app.models.user import User  # Importa la clase User del modelo

import os 



@images_bp.route('/upload', methods=['POST'])
def upload_image():
    # Lógica para cargar imágenes
    # ...
    return jsonify({'access_token': "access_token"}), 200

@images_bp.route('/process', methods=['GET'])
def process_image():
    # Lógica para procesar imágenes utilizando OCR
    # ...
    return jsonify({'access_token': '/process'}), 200




# Función para verificar la extensión de archivo permitida
def allowed_file_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

# Función para generar un nombre de archivo único (puedes ajustar esto según tus necesidades)
def generate_unique_filename(filename):
    import uuid
    unique_filename = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1].lower()
    return unique_filename


# Ruta para la página de actualización de imagen de perfil
@images_bp.route('/updateImage', methods=['GET'])
def viewUpdateImage():
    return render_template('updateImage.html')

# Ruta para actualizar la imagen de perfil
@images_bp.route('/update_profile_picture', methods=['POST'])
@jwt_required()  # Requiere autenticación mediante JWT
def update_profile_picture():
    try:
        current_user_id = get_jwt_identity()  # Obtiene el ID del usuario a partir del token JWT

        # Verifica si el usuario existe en la base de datos
        user = User.query.get(current_user_id)
        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        foto = request.files.get('foto')  # Obtiene el nuevo archivo de imagen cargado

        # Verifica si se proporcionó una nueva imagen
        if foto:
            # Verifica si la extensión del archivo es válida (por ejemplo, solo permite imágenes JPEG)
            if not allowed_file_extension(foto.filename):
                return jsonify({'message': 'Tipo de archivo no permitido para la imagen'}), 400
            

            # Crea el directorio de destino si no existe
            profile_pictures_folder = os.path.join(app.config['PROFILE_PICTURES_FOLDER'], '')
            os.makedirs(profile_pictures_folder, exist_ok=True)

            # Genera un nombre único para la nueva imagen de perfil
            unique_filename = generate_unique_filename(foto.filename)

            # Guarda la nueva imagen en el directorio de imágenes de perfil
            foto.save(os.path.join(app.config['PROFILE_PICTURES_FOLDER'], unique_filename))

            # Actualiza el nombre del archivo de imagen en la base de datos
            user.foto = unique_filename
            db.session.commit()

        return jsonify({'message': 'Imagen de perfil actualizada exitosamente',
                        'nameImage': unique_filename}), 200
    except Exception as e:
        return jsonify({'message': 'Error al actualizar la imagen de perfil', 'error': str(e)}), 500
    

@images_bp.route('/get_profile_picture/<image_name>')
def get_profile_picture(image_name):

    image_path = os.getcwd()+'/'+app.config['PROFILE_PICTURES_FOLDER'] +"/" +image_name
    
    print(image_path)
    # Verifica si el archivo de imagen existe
    if os.path.isfile(image_path):
        # Devuelve la imagen como una respuesta
        return send_file(image_path, mimetype='image/jpeg')  # Ajusta el mimetype según el tipo de imagen
    else:
        # Devuelve una respuesta de error si la imagen no existe
        return 'Imagen no encontrada', 404
    