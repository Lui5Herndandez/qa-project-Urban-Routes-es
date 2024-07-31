# Proyecto Urban Routes Automation

## Descripción del Proyecto
Este proyecto automatiza la reserva de taxis utilizando la página de Urban Routes.
El script realiza una serie de acciones como seleccionar la ruta, añadir el número de teléfono, seleccionar el método de pago ,enviar un mensaje al conductor, usar botones para solicitar mantas y helados. 
Utiliza Selenium para automatizar las interacciones con la página web.

## Tecnologías y Técnicas Utilizadas
- **Lenguaje de Programación**: Python
- **Herramientas de Automatización**: Selenium WebDriver
- **Otras Tecnologías**: ChromeDriver
- **Bibliotecas de Python**:
  - `selenium`
  - `time`
  - `json`

## Estructura del Proyecto
El proyecto está compuesto por los siguientes archivos:
- `data.py`: Contiene los datos necesarios para las pruebas como URL, direcciones, datos de tarjetas, numero de telefono, mensaje al conductor.
- `main.py`: Contiene las clases y métodos principales para realizar la automatización.

## Instrucciones para Ejecutar las Pruebas
1. **Instalar Dependencias**: Asegúrate de tener instaladas todas las dependencias necesarias. Puedes instalarlas usando el siguiente comando:
   ```bash
   pip install selenium
   
##Configuración y Ejecución del Proyecto
- **Clona el repositorio a tu máquina local**
  ```bash
  git clone git@github.com:username/qa-project-Urban-Routes-es.git
- **Ejecutar el archivo**
  ```bash
  pytest folder/archivo.py
