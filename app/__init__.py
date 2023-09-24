from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from sqlalchemy.exc import SQLAlchemyError  # Importa SQLAlchemyError
from dotenv import load_dotenv


app = Flask(__name__)

# Configura la aplicación con la URL de la base de datos desde .env
app.config.from_object('config.Config')

# Crea la instancia de SQLAlchemy
db = SQLAlchemy(app)


# Crea la instancia de JWTManager para la autenticación JWT
jwt = JWTManager(app)


load_dotenv()

migrate = Migrate(app, db)


# Importa las rutas y Blueprints de la aplicación
from app.routes import auth_bp, images_bp  # Asegúrate de importarlos


# Registra los Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(images_bp)
