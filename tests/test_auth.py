import unittest
import time  # Importa el módulo time para medir el tiempo de ejecución
import unittest
from app import app, db  # Asegúrate de importar tu aplicación Flask y db
from app.models import User  # Asegúrate de importar el modelo User
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask import jsonify
import json  # Agrega esta línea para importar el módulo json

class TestAPI(unittest.TestCase):
    def setUp(self):
        # Configura la aplicación para el entorno de pruebas
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        print("test_home")
        # Prueba el endpoint principal ("/") de tu API
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Procesamiento de', response.data)

    def test_db_connection(self):
        # Prueba el servicio de test de conexión a la base de datos ("/test_db_connection")
        print("test_db_connection")
        response = self.app.get('/test_db_connection')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'base de datos exitosa', response.data)

    def test_register_view(self):
        # Prueba la vista de registro ("/register") de tu API
        print("test_register_view")
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registro de Usuario', response.data)  # Verifica que la respuesta contiene código HTML

    def test_login_view(self):
        # Prueba la vista de inicio de sesión ("/login") de tu API
        print("test_login_view")
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)  # Verifica que la respuesta contiene código HTML


    def test_register_new_user(self):
        # Prueba el registro de un nuevo usuario
        print("test_register_new_user")
        user_data = {
            'nombre': 'Crisitann',
            'apellidos': 'Crisitann',
            'dni': 'Crisitann',
            'nick': 'Crisitann',
            'password': 'password123'
        }

        response = self.app.post('/register', json=user_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Nuevo usuario registrado.')

        # Verifica que el usuario se haya guardado en la base de datos
        with app.app_context():
            new_user = User.query.filter_by(dni='12345678A').first()
            self.assertIsNotNone(new_user)




    def test_register_existing_user(self):
        # Crea un usuario a través de la ruta '/register'
        print("test_register_existing_user")
        user_data = {
            'nombre': 'Nombre2',
            'apellidos': 'Apellidos2',
            'dni': '12345678A2',
            'nick': 'usuario12',
            'password': 'password1232'
        }

        response = self.app.post('/register', json=user_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Nuevo usuario registrado.')

        # Intenta registrarlo nuevamente
        response = self.app.post('/register', json=user_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'El usuario ya existe')


    def test_login(self):
        print("test_login")
        # Prueba iniciar sesión con contraseña correcta
        print("Prueba iniciar sesión con contraseña correcta")
        response_valid = self.app.post('/login', json={'nick': 'usuario1', 'password': 'password123'})
        data_valid = json.loads(response_valid.data.decode('utf-8'))
        self.assertEqual(response_valid.status_code, 200)
        self.assertIn('access_token', data_valid)  # Verifica que exista 'access_token' en la respuesta

        # Prueba iniciar sesión con contraseña incorrecta
        print("Prueba iniciar sesión con contraseña incorrecta")
        response_invalid = self.app.post('/login', json={'nick': 'usuarioB', 'password': 'password123'})
        data_invalid = json.loads(response_invalid.data.decode('utf-8'))
        self.assertEqual(response_invalid.status_code, 200)
        self.assertIn('message', data_invalid)  # Verifica que exista 'message' en la respuesta
        self.assertEqual(data_invalid['message'], 'Contraseña incorrecta')

if __name__ == '__main__':
    # Crea un objeto TextTestRunner para mostrar las pruebas de manera más legible
    test_runner = unittest.TextTestRunner(verbosity=2)
    
    # Ejecuta las pruebas y mide el tiempo
    start_time = time.time()
    unittest.main(testRunner=test_runner)
    end_time = time.time()
    
    # Calcula y muestra el tiempo total que tomaron las pruebas
    execution_time = end_time - start_time
    print(f"Tiempo total de ejecución de las pruebas: {execution_time:.2f} segundos")
