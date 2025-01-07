from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

# Configuración del WebDriver
chrome_driver_path = r'C:\SeleniumDrivers\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# URL de la página
url = 'https://drawaria.online/'
driver.get(url)

# Esperar a que la página cargue completamente
time.sleep(5)

# Encontrar el elemento canvas
canvas = driver.find_element(By.ID, 'canvas')

# Función para enviar comandos de dibujo a través de WebSockets
def send_draw_command(text):
    draw_commands = [
        {
            "drawcmd": 0,
            "data": [0.5, 0.5, 0.5, 0.5, True, -2000, "#000000", -1, False]
        }
    ]

    # Convertir los comandos de dibujo a formato JSON
    draw_commands_json = json.dumps(draw_commands)

    # Enviar los comandos de dibujo a través de WebSockets
    driver.execute_script(f"""
        var socket = new WebSocket('wss://drawaria.online/socket.io/?sid1=undefined&hostname=drawaria.online&EIO=3&transport=websocket');
        socket.onopen = function() {{
            socket.send('42{draw_commands_json}');
        }};
    """)

# Bucle para permitir al usuario ingresar y enviar múltiples comandos de dibujo
while True:
    # Permitir al usuario ingresar texto
    user_text = input("Write the text in the canvas OR exit to quit(Only works in private rooms): ")

    if user_text.lower() == 'exit':
        break

    # JavaScript para dibujar el texto ingresado por el usuario en el canvas
    js_code_user_text = f"""
        var canvas = document.getElementById('canvas');
        var ctx = canvas.getContext('2d');
        ctx.font = '48px serif';
        ctx.fillStyle = 'black';  // Establecer el color del texto a negro
        ctx.fillText('{user_text}', 50, 100);
    """

    # Ejecutar el JavaScript en el contexto de la página
    driver.execute_script(js_code_user_text)

    # Enviar los comandos de dibujo a través de WebSockets
    send_draw_command(user_text)

    # Esperar un momento para que el texto se dibuje
    time.sleep(2)

# Cerrar el navegador
driver.quit()
