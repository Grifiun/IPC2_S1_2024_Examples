import xml.etree.ElementTree as ET
from xml_service.xml_handler import XMLHandler

class XMLTree(XMLHandler):
    def create_xml_node(self, name):
        # Crear un elemento (si es el primero será la raíz)
        node = ET.Element(name)
        return ET.ElementTree(node), node

    def write_xml(self, xml_element, file_path):
        # Crear un objeto ElementTree
        tree = ET.ElementTree(xml_element)

        # Agregar la declaración XML manualmente
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_content = ET.tostring(xml_element, encoding='utf-8').decode('utf-8')
        xml_with_declaration = xml_declaration + xml_content

        # Escribir el árbol XML en el archivo
        with open(file_path, 'w') as file:
            file.write(xml_with_declaration)

        print(f"Datos guardados en '{file_path}'")

    def load_xml(self, file_path):
        # Parsear el archivo XML
        tree = ET.parse(file_path)

        # Obtener el elemento raíz del árbol
        root_node = tree.getroot()

        return root_node

    def add_child_to_node(self, parent_doc, parent_node, child):
        # Agregar el nodo hijo al nodo padre
        parent_node.append(child)

    def add_text_to_node(self, parent_doc, parent_node, text):
        # Crear un elemento con texto
        child = ET.Element(parent_node.tag)
        child.text = text

        # Agregar el nodo hijo al nodo padre
        self.add_child_to_node(parent_doc, parent_node, child)

    def create_and_append_node_with_text_to_node(self, parent_doc, parent_node, name, text):
        # Crear un elemento con texto
        child = ET.Element(name)
        child.text = text

        # Agregar el nodo hijo al nodo padre
        self.add_child_to_node(parent_doc, parent_node, child)

    def print_xml_node(self, node, indent=""):
        # Convertir el árbol ElementTree a una cadena
        xml_str = ET.tostring(node, encoding="unicode")

        # Imprimir el nodo XML
        print(xml_str)

    def get_node_text(self, node):
        # Obtener el texto del nodo
        return node.text

    def get_node_text_by_tag(self, node, tag_name):
        # Buscar un nodo por su etiqueta
        child_node = node.find(tag_name)
        if child_node is not None:
            return self.get_node_text(child_node)
        return None

    def read_and_print_xml(self, file_path):
        try:
            # Cargar el archivo XML utilizando ElementTree
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Imprimir el nodo raíz y sus hijos
            self.print_xml_node(root)
        except ET.ParseError as e:
            print(f"Error al procesar el archivo XML: {e}")

    def modify_node_text(self, node, new_text):
        # Modificar el texto del nodo
        node.text = new_text

    def get_xml_node_by_tag(self, root_node, tag_name):
        # Buscar un nodo por su etiqueta
        return root_node.find(tag_name)

    def get_xml_node_list_by_tag(self, root_node, tag_name):
        # Buscar todos los nodos por su etiqueta
        return root_node.findall(tag_name)
        # return root_node.iterfind('.//' + tag_name)

    def update_xml_node_value_by_tag(self, root_node, tag_name, new_value):
        node = self.get_xml_node_by_tag(root_node, tag_name)
        if node is not None:
            node.text = new_value

# Verifica si este archivo es el punto de entrada principal
if __name__ == "__main__":
    # Puedes agregar código aquí para probar la funcionalidad de la clase si lo deseas
    pass
