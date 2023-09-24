import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'tu_clave_secreta_predeterminada')
    # Database URI
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@127.0.0.1:5432/l3v3lupt3k'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'tu_jwt_secreto_predeterminado')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
   # Extensiones de archivo permitidas para las imágenes
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    # Carpeta donde se guardarán las fotos de perfil
    PROFILE_PICTURES_FOLDER =  os.getenv('UPLOAD_FOLDER', 'profile_pictures')# Configura la ubicación del token en una cookie con un nombre específico
    JWT_TOKEN_LOCATION  = ['headers', 'cookies']
    JWT_ACCESS_COOKIE = 'jwt_token'  # Nombre de la cookie del token
