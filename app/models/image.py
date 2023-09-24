from app import db  # Asegúrate de importar la instancia de la base de datos 'db' desde la aplicación Flask

class Image(db.Model):
    __tablename__ = 'images'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    fecha_registro = db.Column(db.DateTime)
    ubicacion = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __init__(self, fecha_registro, ubicacion, user_id):
        self.fecha_registro = fecha_registro
        self.ubicacion = ubicacion
        self.user_id = user_id
        

    def __repr__(self):
        return f"<Image {self.user_id}>"