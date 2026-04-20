# PROYECTO SPRINT 8
## Automatización de pruebas con la API "Urban Grocers"
Por: Karen Lozano

Este proyecto tiene como ojetivo automatizar pruebas para el endpoint de creación de kits de la API de Urban Grocers, validando específicamente el parámetro "name".
Se desarrollaron pruebas positivas y negativas basadas en la lista de comprobación proporcionada por el bootcamp, con el fin de verificar el comportamiento del sistema ante distintos tipos de entrada.
Las pruebas implementaron utilizando Python y Pytest, enviando solicitudes HTTP reales al servidor proporcionado.

## Tecnologías usadas
- Python
- Pytest
- PyCharm (IDE)
- Git y GitHub

## Estructura del proyecto
- configuration.py -> Contiene la URL base y las rutas de los endpoints.
- data.py -> Contiene los cuerpos de solicitud y los headers.
- sender_stand_request.py -> Contiene las funciones para enviar solicitudes POST y obtener el Token.
- create_kit_name_kit_test.py -> Contiene las pruebas automatizadas del parámetro "name".
- README.md -> Contiene la documentación del proyecto.
- .gitignore -> Contiene archivos excluidos del repositorio.

## Instalación
Instalar librerias pytest y requests:
```sh
pip3 install pytest
pip3 install requests
```

o instalar desde requests.txt
```sh
pip3 install -r requirements.txt
```

## Ejecución de pruebas
Para ejecutar todas las pruebas:
```sh
pytest
```
Para ejecutar un archivo en específico:
```sh
pytest create_kit_name_kit_test.py -v
```

## Flujo de pruebas
Se desarrollaron 9 pruebas basadas en la lista de comprobación:
### Casos positivos (HTTP esperado = 201)
- Longitud mínima permitida (1 caracter)
- Longitud máxima permitida (511 caracteres)
- Uso de caracteres especiales
- Uso de espacios
- Uso de números como string

### Casos negativos (HTTP esperado = 400)
- Nombre vacío (0 caracteres)
- Nombre mayor al límite permitido (512 caracteres)
- Parámetro "name" ausente
- Tipo de dato incorrecto (carácter numérico)

## Análisis
Las pruebas permiten verificar:
- Comportamiento del endpoint ante entradas válidas.
- MAnejo de validaciones de longitud.
- Validación del tipo de dato.
- Respuesta del servidor ante datos faltantes.

## Conclusión
El proyecto implementa pruebas automatizadas que validan el parámetro "name" en la creación de kits dentron de la API de Urban Grocers.
Se cubren escenarios positivos y negativos según la lista de comprobaci´n proporcionada, permotiendo evaluar la consistencia de las respuestas del servidor y detectar comportamientos inesperados.
La automatización facilita la repetición de pruebas y mejora la confiabilidad del proceso de validación ante cambios futuros del backend.