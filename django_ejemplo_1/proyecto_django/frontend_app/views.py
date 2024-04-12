from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET
import re

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def formulario(request):
    context = {}
    return render(request, 'formulario.html', context)

def formulario_nombre(request):
    context = {}
    return render(request, 'formulario_nombre.html', context)

def procesar_formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        carnet = request.POST.get('carnet')
        match = re.search(r'[0-9]{9}', carnet)
        if match:
            carnet = match.group() # Actualiza el valor de carnet con el resultado de la búsqueda
            print("CARNET:", carnet)
        else:
            print("No se encontró un carné válido.")

        print("nombre:", nombre, "carnet:", carnet)
        context = {'nombre': nombre, 'carnet': carnet}
        return render(request, 'datos.html', context)
    else:
        return HttpResponseBadRequest("Bad request")

def procesar_formulario_nombre(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('nombre')
            country = 'GT'

            # Crear el XML con los datos
            root = ET.Element('data')
            ET.SubElement(root, 'name').text = name
            ET.SubElement(root, 'country').text = country
            xml_data = ET.tostring(root)

            api_url_flask_backend = 'http://127.0.0.1:5000/recibirNombre'
            headers = {'Content-Type': 'application/xml'}
            
            # Enviar los datos XML al backend Flask
            result_xml = requests.post(api_url_flask_backend, data=xml_data, headers=headers)

            # Analizar el XML recibido del backend Flask
            root = ET.fromstring(result_xml.text)
            genero = root.find('.//gender').text
            edad = root.find('.//age').text

            # Realizar los ifs necesarios y establecer el contexto
            genero = "Hombre" if genero == "male" else "Mujer"
            context = {'nombre': name, 'genero': genero, 'edad': edad}

            return render(request, 'datos_edad.html', context)
        except Exception as e:
            return HttpResponseBadRequest(f'Error: {str(e)}')
    else:
        return HttpResponseBadRequest("Bad request")
    

