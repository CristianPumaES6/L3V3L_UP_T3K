from app import db  # Importa la instancia de SQLAlchemy

class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellidos = db.Column(db.String(255))
    dni = db.Column(db.String(9), unique=True, nullable=False)
    nick = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255))  # Ruta o nombre de archivo de la foto

    # Puedes agregar relaciones con otras tablas aquí si es necesario
    # Ejemplo: posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, nombre, apellidos, dni, nick, password, foto=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.nick = nick
        self.password = password
        self.foto = foto

    def __repr__(self):
        return f"<User {self.nick}>"