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
