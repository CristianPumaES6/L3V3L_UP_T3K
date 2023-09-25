# Usamos la imagen base de Python
FROM python:3.8-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos requeridos al directorio de trabajo
COPY . .

COPY run_migration.sh .


# Damos permisos de ejecución al script
RUN chmod +x run_migration.sh

# Instala Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Explicamos el puerto que debe exponer la aplicación
EXPOSE 5000

# Comando para ejecutar el script de migración
CMD ["./run_migration.sh"]
