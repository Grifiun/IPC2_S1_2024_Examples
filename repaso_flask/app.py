from flask import Flask, render_template, send_from_directory, request, jsonify, Response
import requests

app = Flask(__name__)

# Configurar el middleware para servir archivos estáticos desde las carpetas 'styles' y 'scripts'
@app.route('/styles/<path:filename>')
def styles(filename):
    return send_from_directory('styles', filename)

@app.route('/scripts/<path:filename>')
def scripts(filename):
    return send_from_directory('scripts', filename)

# Endpoints
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/formulario_nombre')
def formulario_nombre():
    return render_template('formulario_nombre.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    carnet = request.form['carnet']

    print("nombre: ", nombre, " carnet: ", carnet)
    return render_template('datos.html', nombre = nombre, carnet = carnet)

@app.route('/procesar_formulario_nombre', methods=['POST'])
def procesar_formulario_nombre():
    try:
        name = request.form['nombre']
        country = 'GT'

        api_url_genero = f'https://api.genderize.io?name={name}&country_id={country}'
        api_url_edad = f'https://api.agify.io?name={name}&country_id={country}'

        result_genero = requests.get(api_url_genero).json()
        result_edad = requests.get(api_url_edad).json()

        genero = "Hombre" if result_genero['gender'] == "male" else "Mujer"
        edad = result_edad['age']

        print(genero, "   ", edad)

        return render_template('datos_edad.html', nombre = name, genero = genero, edad = edad), 200
    except Exception as e:
        return f'Error: {str(e)}', 400

if __name__ == '__main__':
    app.run(debug=True)

