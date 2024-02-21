import xml.dom.minidom
from xml_service.xml_handler import XMLHandler
class XMLDom(XMLHandler):
    def create_xml_node(self, name):
        # Crear un documento XML
        doc = xml.dom.minidom.Document()

        # Crear un elemento (si es el primero será la raíz)
        node = doc.createElement(name)
        doc.appendChild(node)

        return doc, node

    def write_xml(self, doc, file_path):
        with open(file_path, 'w') as file:
            doc.writexml(file)

    def load_xml(self, file_path):
        # Parsear el archivo XML
        doc = xml.dom.minidom.parse(file_path)

        # Obtener el elemento raíz del documento
        root_node = doc.documentElement

        return root_node

    def add_child_to_node(self, parent_doc, parent_node, child):
        # Agregar el nodo de texto como hijo al nodo padre
        parent_node.appendChild(child)

    def add_text_to_node(self, parent_doc, parent_node, text):
        # Crear un nodo de texto
        text_node = parent_doc.createTextNode(text)

        # Agregar el nodo de texto como hijo al nodo padre
        self.add_child_to_node(parent_doc, parent_node, text_node)

    def create_and_append_node_with_text_to_node(self, parent_doc, parent_node, tag_name, text):
        _, node_text = self.create_xml_node(tag_name)
        self.add_text_to_node(parent_doc, node_text, text)
        self.add_child_to_node(parent_doc, parent_node, node_text)

    def print_xml_node(self, node, indent=""):
        # Crear un documento XML legible
        xml_str = node.toprettyxml(indent=indent)

        # Imprimir el nodo XML
        print(xml_str)

    def get_node_text(self, node):
        # Verificar si se encontraron nodos con la etiqueta
        if node:
            # Obtener el texto del nodo
            if node.firstChild and node.firstChild.nodeType == node.TEXT_NODE:
                return node.firstChild.nodeValue

        # Retornar None si no se encuentra el nodo con la etiqueta especificada
        return None

    def get_node_text_by_tag(self, node, tag_name):
        # Buscar un nodo por su etiqueta
        nodes = node.getElementsByTagName(tag_name)
        if nodes:
            return self.get_node_text(nodes[0])  # devuelve el listado entero
        return None  # Devuelve None si no se encuentra el nodo

    def read_and_print_xml(self, file_path):
        try:
            # Imprimir el nodo raíz y sus hijos
            self.print_xml_node(self.load_xml(file_path))
        except Exception as e:
            print(f"Error al procesar el archivo XML: {e}")

    def modify_node_text(self, node, new_text):
        # Modificar el texto del nodo
        if node.firstChild.nodeType == node.TEXT_NODE:
            node.firstChild.data = new_text
        else:
            # Si el nodo no tiene un nodo de texto, agregar uno nuevo
            text_node = node.ownerDocument.createTextNode(new_text)
            node.appendChild(text_node)

    def get_xml_node_by_tag(self, root_node, tag_name):
        # Buscar un nodo por su etiqueta
        nodes = root_node.getElementsByTagName(tag_name)
        if nodes:
            return nodes[0]  # Devuelve el primer nodo encontrado
        return None  # Devuelve None si no se encuentra el nodo

    def get_xml_node_list_by_tag(self, root_node, tag_name):
        # Buscar un nodo por su etiqueta
        nodes = root_node.getElementsByTagName(tag_name)
        if nodes:
            return nodes  # devuelve el listado entero
        return None  # Devuelve None si no se encuentra el nodo

    def update_xml_node_value_by_tag(self, root_node, tag_name, new_value):
        node = self.get_xml_node_by_tag(root_node, tag_name)
        if node is not None:
            node.firstChild.nodeValue = new_value

# Verifica si este archivo es el punto de entrada principal
if __name__ == "__main__":
    # Puedes agregar código aquí para probar la funcionalidad de la clase si lo deseas
    pass
