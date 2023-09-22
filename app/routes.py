from flask import render_template
from app import app

@app.route('/')
def index():
    mensaje = "¡Hola, mundo!"
    return render_template('index.html', mensaje=mensaje)
