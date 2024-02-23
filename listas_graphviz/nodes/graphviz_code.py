class GraphvizCode:
    def __init__(self):
        pass

    def get_graphviz_code(self, node):
        string_graphviz_code = "digraph g {\nnode [shape = record,height=.1];\n"

        string_graphviz_code += self.node_to_string_graphviz_code(node)

        string_graphviz_code += "}\n"
        return string_graphviz_code

    def node_to_string_graphviz_code(self, node):
        node_string_graphviz_code = f"\n\tnode{node.node_id}[label = \"<f0> |<f1> {node.node_value}|<f2> \"]"

        if node.next_node is not None:
            node_string_graphviz_code += f"\n\t\"node{node.node_id}\":f0 -> \"node{node.next_node.node_id}\":f1;"
            # Esta linea itera, sin embargo, si retorna al nodo root que inicio todo en una lista circular,
            #  este se quedara en un bucle infinito
            node_string_graphviz_code += self.node_to_string_graphviz_code(node.next_node)

        if node.prev_node is not None:
            node_string_graphviz_code += f"\n\t\"node{node.node_id}\":f0 -> \"node{node.prev_node.node_id}\":f1;"

        return node_string_graphviz_code
