# L3V3L_UP_T3K


Este proyecto es una aplicación web construida con Flask que se ejecuta en un contenedor Docker. En este contenedor Docker, además de la aplicación Flask que ocupa el puerto 5000, se ejecutan una base de datos PostgreSQL en el puerto 5432 y pgAdmin en el puerto 80. A continuación, se detallan los pasos para levantar la aplicación desde el contenedor.


## Requisitos previos

Antes de continuar, asegúrate de tener instalados los siguientes requisitos en tu sistema:

- Docker: [Instrucciones de instalación de Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación de Docker Compose](https://docs.docker.com/compose/install/)
- Tesseract OCR: [Instrucciones de instalación de Tesseract OCR](https://github.com/tesseract-ocr/tesseract)


## Pasos para ejecutar la aplicación

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
6. Además, puedes acceder a la interfaz de administración de PostgreSQL a través de:
    ```bash
    ```
7. Utiliza las credenciales predeterminadas para PostgreSQL
    ```bash
    (usuario: root, contraseña: root) para acceder.
    ```
## Flujo de Pantallas

A continuación, se presenta el flujo de pantallas de nuestro proyecto "L3V3L_UP_T3K" con sus vistas específicas:

1. **Pantalla de Inicio / Inicio de Sesión**
   - **Rutas:** `/` y `/login`
   - Esta es la pantalla de inicio de la aplicación.
   - Proporciona información general sobre el proyecto y ofrece un formulario de inicio de sesión. También incluye una opción para redireccionar al formulario de registro.

2. **Pantalla de Registro**
   - **Ruta:** `/registro`
   - Los usuarios pueden registrarse desde esta pantalla.
   - Después del registro, son redirigidos automáticamente al formulario de inicio de sesión.

3. **Actualizar Imagen de Perfil**
   - **Ruta:** `/updateImage`
   - Se requiere un token de autenticación para acceder a esta pantalla.
   - Permite a los usuarios actualizar su foto de perfil.

4. **Imágenes del Usuario**
   - **Ruta:** `/userImages`
   - Se requiere un token de autenticación para acceder a esta pantalla.
   - Muestra las imágenes subidas por el usuario.
   - Ofrece la funcionalidad para procesar una imagen y obtener los caracteres contenidos en ella.

Este es el flujo de pantallas detallado de nuestro proyecto "L3V3L_UP_T3K". Cada vista se representa con sus rutas correspondientes y una breve descripción de su funcionalidad. Asegúrate de ajustar las rutas y descripciones según las características específicas de tu proyecto.
