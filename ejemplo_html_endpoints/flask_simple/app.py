from flask import Flask, render_template, send_from_directory, request, jsonify, Response
import requests
from graphviz import Digraph

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

@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    # Obtener el número del cuerpo de la solicitud
    number = request.json.get('number')

    # Verificar si se proporcionó un número
    if number is None:
        return Response('Se necesita proporcionar un número en el cuerpo de la solicitud.', status=400)

    # Inicializar el objeto Digraph de Graphviz
    dot = Digraph(comment='Bloque generado')
    

    # Generar los nodos/bloques con las coordenadas especificadas
    for x in range(number):
        for y in range(number):
            dot.node(f'{x}_{y}', f'({x}, {y})', shape='square')

    # Agregar las conexiones entre nodos
    for x in range(number - 1):
        for y in range(number):
            dot.edge(f'{x}_{y}', f'{x+1}_{y}')
            dot.edge(f'{y}_{x}', f'{y}_{x+1}')

    # Alinear los nodos en filas y columnas
    for x in range(number):
        with dot.subgraph() as s:
            s.attr(rank='same')
            for y in range(number):
                s.node(f'{x}_{y}')

    # Renderizar el gráfico y devolverlo como una respuesta
    return Response(dot.source)

if __name__ == '__main__':
    app.run(debug=True)

