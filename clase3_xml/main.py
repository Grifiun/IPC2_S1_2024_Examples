print("Mensaje desde develop")

from xml_dom.xml_dom import create_xml_node, add_child_to_node, print_xml_node

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un nodo llamado 'root'
    doc, root_node = create_xml_node("root")

    # Agregar texto al nodo 'root'
    # add_child_to_node(doc, root_node, "Contenido del root")

    # Crear un nodo hijo llamado 'child1'
    _, child1_node = create_xml_node("child1")

    # Agregar texto al nodo 'child1'
    add_child_to_node(doc, child1_node, "Contenido del child1")

    # Agregar 'child1' como hijo de 'root'
    root_node.appendChild(child1_node)

    # Imprimir el nodo 'root' y sus hijos
    print_xml_node(doc, root_node)