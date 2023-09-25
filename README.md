
# L3V3L_UP_T3K  🚀


Este proyecto es una aplicación web construida con Flask que se ejecuta en un contenedor Docker. En este contenedor Docker, además de la aplicación Flask que ocupa el puerto 5000, se ejecutan una base de datos PostgreSQL en el puerto 5432 y pgAdmin en el puerto 80. A continuación, se detallan los pasos para levantar la aplicación desde el contenedor.


## Requisitos previos 🛠️

Antes de continuar, asegúrate de tener instalados los siguientes requisitos en tu sistema:

- Docker: [Instrucciones de instalación de Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación de Docker Compose](https://docs.docker.com/compose/install/)
- Tesseract OCR: [Instrucciones de instalación de Tesseract OCR](https://github.com/tesseract-ocr/tesseract)


## Pasos para ejecutar la aplicación 🏃‍♂️

1. Clona este repositorio en tu sistema:

   ```bash
        git clone https://github.com/CristianPumaES6/L3V3L_UP_T3K.git
    ```

2. Navega hasta el directorio del proyecto:
    ```bash
        cd L3V3L_UP_T3K
    ```

3. Construye la imagen Docker utilizando el siguiente comando:

    ```bash
        docker-compose build
    ```

4. Inicia los contenedores utilizando el siguiente comando:
    ```bash
        docker-compose up
    ```
5. Una vez que los contenedores estén en funcionamiento, podrás acceder a la aplicación Flask en tu navegador web utilizando la siguiente URL:
    ```bash
        http://localhost:5000/
    ```
6. Ahora, debemos acceder a la interfaz de administración de PostgreSQL a través del navegador:
    ```bash
         http://localhost/
    ```
7. Utiliza las credenciales predeterminadas para PostgreSQL
    ```bash
    (usuario: admin@admin.com, contraseña: admin) para acceder.
    ```
8. Luego crearemos una nueva conexion
    ```bash
    (Hostname: postgrest
    port: 5432
    maintenance: root
    username: root
    psw: root
   )
    ```

8. Luego creamos nuestro nueva base datos

    ```bash
      l3v3lupt3k
    ```
   <img width="300" alt="image" src="https://github.com/CristianPumaES6/L3V3L_UP_T3K/assets/29841048/828277cd-5359-4dfb-9832-df17b6c340c3">
 
9. volvemos a ejecutar docker
    ```bash
        docker-compose up
    ```

10. Verificamos que las talblas users y imagenes se hallan creado correctamente
    ```bash
         http://localhost/
    ```



# Flujo de Pantallas  🖥️


## A continuación, se presenta el flujo de pantallas de nuestro proyecto "L3V3L_UP_T3K" con sus vistas específicas:

1. **Pantalla de Inicio / Inicio de Sesión**
   - **Rutas:** `/` y `/login`
   - Esta es la pantalla de inicio de la aplicación.
   - Proporciona información general sobre el proyecto y ofrece un formulario de inicio de sesión. También incluye una opción para redireccionar al formulario de registro.
<img width="571" alt="image" src="https://github.com/CristianPumaES6/L3V3L_UP_T3K/assets/29841048/69b71a8e-2543-4691-8575-cf348c54714a">

2. **Pantalla de Registro** 📝
   - **Ruta:** `/registro`
   - Los usuarios pueden registrarse desde esta pantalla.
   - Después del registro, son redirigidos automáticamente al formulario de inicio de sesión.
<img width="691" alt="image" src="https://github.com/CristianPumaES6/L3V3L_UP_T3K/assets/29841048/61842a8a-69a1-4a5b-bbb6-98bbbf6e261b">

3. **Actualizar Imagen de Perfil** 📷
   - **Ruta:** `/updateImage`
   - Se requiere un token de autenticación para acceder a esta pantalla.
   - Permite a los usuarios actualizar su foto de perfil.

4. **Imágenes del Usuario**  🖼️ 🖼️ 🖼️
   - **Ruta:** `/userImages`
   - Se requiere un token de autenticación para acceder a esta pantalla.
   - Muestra las imágenes subidas por el usuario.
   - Ofrece la funcionalidad para procesar una imagen y obtener los caracteres contenidos en ella.


### Los servicios expuesttos para el uso de escalar el aplicativo a otros entornos son 

#### Ruta para Cargar Imágenes por usuario📷


@images_bp.route('/add_photo_user', methods=['POST'])

- Permite a los usuarios cargar imágenes a sus cuentas.
- Verifica la extensión del archivo y almacena la imagen en el directorio correspondiente.
- Asocia la imagen cargada a la cuenta del usuario en la base de datos.

#### Ruta para Procesar Imágenes mediante OCR 🖋️

@images_bp.route('/processImage', methods=['POST'])

- Permite a los usuarios procesar una imagen seleccionada y extraer texto de la misma utilizando OCR.
- Verifica la existencia del archivo de imagen, la procesa y devuelve el texto extraído como respuesta JSON.

####  Vista de Imagen procesada por el Usuario de Fibonacci 🖼️
<img width="1373" alt="image" src="https://github.com/CristianPumaES6/L3V3L_UP_T3K/assets/29841048/631c8788-81ba-4428-8c48-58f887d29b14">

:::::
