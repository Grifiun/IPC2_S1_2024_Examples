from flask import Flask, render_template, send_from_directory

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

if __name__ == '__main__':
    app.run(debug=True)

