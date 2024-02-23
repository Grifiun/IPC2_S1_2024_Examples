from nodes.node import Node
from nodes.graphviz_code import GraphvizCode

if __name__ == '__main__':
    # node simplemente enlazada

    node0 = Node("node 0")
    node1 = Node("node 1", node0)
    node2 = Node("node 2", node1)
    node3 = Node("node 3", node2)

    # Siguientes
    node0.next_node = node1
    node1.next_node = node2
    node2.next_node = node3

    # Anteriores
    node3.prev_node = node2
    node2.prev_node = node1
    node1.prev_node = node0

    # Una lista circularmente enlazada generará que el siguiente algoritmo se quede en bucle infinito
    graphviz_code = GraphvizCode()
    print(graphviz_code.get_graphviz_code(node0))

