from flask import request, jsonify
from app.routes import images_bp

@images_bp.route('/upload', methods=['POST'])
def upload_image():
    # Lógica para cargar imágenes
    # ...
    return jsonify({'access_token': access_token}), 200

@images_bp.route('/process/<int:image_id>', methods=['GET'])
def process_image(image_id):
    # Lógica para procesar imágenes utilizando OCR
    # ...
    return jsonify({'access_token': access_token}), 200
