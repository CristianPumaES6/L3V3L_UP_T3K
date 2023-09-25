se crearos los issue de git.


Para la base de datpos postgresql 


pip install psycopg2-binary


// levantar pyton con sus depencdencias
source venv/bin/activate

pip install python-dotenv
pip install Flask-Migrate

docker-compose up -d




Ejecuta el siguiente comando en la terminal para crear una migración inicial:

csharp
Copy code
flask db init

flask db mirgate -m 'Initial Migration'

Luego, genera una migración con el siguiente comando:

arduino
Copy code
flask db migrate -m "Create users table"
Esto generará un archivo de migración en el directorio /migrations/versions.

Aplica la migración a tu base de datos con el siguiente comando:

Copy code
flask db upgrade
Esto creará la tabla "users" en tu base de datos de acuerdo con la definición en tu modelo User.

PRoblemas con con version migrate
2.There seems to be issues with latest Flask-Migrate. So use this command pip install --force-reinstall -v "Flask-Migrate==3.1.0"

flask db init
flask db migrate -m "Initial migration"
flask db upgrade



las rutas privadas las protegemos con JWT 

elimine 
Werkzeug==2.3.7


//si borramos lel directorio venv
python -m venv venv

python3 run.py


uso de decoradores


LO MAS COMPLICADO INSTALR tesseract is not installed or it's not in your PATH. See README file for more information

lo instale dezsde brem 
brew install tesseract