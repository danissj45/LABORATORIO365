from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    # Aquí puedes agregar la lógica para verificar la contraseña
    if password == '12345678':  # Reemplaza con tu contraseña
        return render_template('success.html', password=password)
    else:
        return render_template('index.html', error='Contraseña incorrecta')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4300)
