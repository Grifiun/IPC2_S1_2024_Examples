from flask import Flask, render_template, send_from_directory, request, jsonify, Response
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/recibirNombre', methods=['POST'])
def recibir_nombre():
    try:
        # Obtener los datos XML de la solicitud
        xml_data = request.data
        print("DATA RECEIVED: ", xml_data)

        # Procesar los datos XML
        root = ET.fromstring(xml_data)
        name = root.find('name').text
        country = root.find('country').text

        # Realizar las solicitudes a las API
        api_url_genero = f'https://api.genderize.io?name={name}&country_id={country}'
        api_url_edad = f'https://api.agify.io?name={name}&country_id={country}'

        result_genero = requests.get(api_url_genero).json()
        result_edad = requests.get(api_url_edad).json()

        # Crear el resultado final como XML
        root = ET.Element('resultados')
        resultados_edad = ET.SubElement(root, 'resultados_edad')
        for key, value in result_edad.items():
            ET.SubElement(resultados_edad, key).text = str(value)
        resultados_genero = ET.SubElement(root, 'resultados_genero')
        for key, value in result_genero.items():
            ET.SubElement(resultados_genero, key).text = str(value)

        # Convertir el resultado final a XML
        xml_response = ET.tostring(root)
        print ("DATA RETORNADA:", xml_response)

        return xml_response, 200, {'Content-Type': 'application/xml'}
    except Exception as e:
        print (f'Error: {str(e)}', 400)
        return f'Error: {str(e)}', 400

if __name__ == '__main__':
    app.run(debug=True)

