:::::
## Nuevas Rutas y Funcionalidades

### Carga de Imágenes y Procesamiento OCR

Se han implementado las siguientes rutas y funcionalidades:

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
