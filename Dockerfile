# Usamos la imagen base de Python
FROM python:3.8-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos requeridos al directorio de trabajo
COPY . .

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Explicamos el puerto que debe exponer la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "run.py"]
