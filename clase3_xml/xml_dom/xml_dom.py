# Encargar de crear archivos xml y manejarlos

import xml.dom.minidom

def create_xml_node(name):
    # Crear un documento XML
    doc = xml.dom.minidom.Document()

    # Crear un elemento raíz
    node = doc.createElement(name)
    doc.appendChild(node)

    return doc, node

def add_child_to_node(parent_doc, parent_node, child):
    # Crear un nodo de texto
    text_node = parent_doc.createTextNode(child)

    # Agregar el nodo de texto como hijo al nodo padre
    parent_node.appendChild(text_node)

def print_xml_node(doc, node, indent=""):
    # Crear un documento XML legible
    xml_str = node.toprettyxml(indent=indent)

    # Imprimir el nodo XML
    print(xml_str)

def read_and_print_xml(file_path):
    try:
        # Parsear el archivo XML
        doc = xml.dom.minidom.parse(file_path)

        # Obtener el elemento raíz del documento
        root_node = doc.documentElement

        # Imprimir el nodo raíz y sus hijos
        print_xml_node(doc, root_node)
    except Exception as e:
        print(f"Error al procesar el archivo XML: {e}")