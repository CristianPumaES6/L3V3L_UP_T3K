import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'tu_clave_secreta_predeterminada')
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@127.0.0.1:5432/root'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'tu_jwt_secreto_predeterminado')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')