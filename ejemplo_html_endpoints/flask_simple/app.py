from flask import Flask, render_template, send_from_directory, request, jsonify
import requests

app = Flask(__name__)

# Configurar el middleware para servir archivos estáticos desde las carpetas 'styles' y 'scripts'
@app.route('/styles/<path:filename>')
def styles(filename):
    return send_from_directory('styles', filename)

@app.route('/scripts/<path:filename>')
def scripts(filename):
    return send_from_directory('scripts', filename)

@app.route('/hola')
def hola():
    return "Hola"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recibirNombre', methods=['GET'])
def recibir_nombre():
    try:
        name = request.args.get('name')
        country = 'GT'

        api_url_genero = f'https://api.genderize.io?name={name}&country_id={country}'
        api_url_edad = f'https://api.agify.io?name={name}&country_id={country}'

        result_genero = requests.get(api_url_genero).json()
        result_edad = requests.get(api_url_edad).json()

        result_final = {
            'resultados_edad': result_edad,
            'resultados_genero': result_genero
        }

        return jsonify(result_final), 200
    except Exception as e:
        return f'Error: {str(e)}', 400


if __name__ == '__main__':
    app.run(debug=True)

