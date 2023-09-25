#!/bin/sh

# Ejecuta las migraciones
flask db init
flask db migrate  
flask db upgrade

  
echo "------------------------------"
echo "--------{  RUN.PY  }---------"
echo "------------------------------"

# Inicia la aplicación Flask
python run.py