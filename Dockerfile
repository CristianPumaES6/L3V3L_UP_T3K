# Usa una imagen de Python como base
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY app.py .

# Instala las dependencias de Flask
RUN pip install Flask

# Expón el puerto 5000 para que Flask pueda recibir solicitudes
EXPOSE 5000

# Ejecuta la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]