class Node:
    def __init__(self, node_value, prev_node=None, next_node=None):
        self.node_id = 0 if prev_node is None else (prev_node.node_id + 1)
        self.node_value = node_value
        self.next_node = next_node
        self.prev_node = prev_node

    def __iter__(self):
        # Iniciar el iterador desde el node actual
        self.current_node = self
        return self

    def __next__(self):
        # Si hay un siguiente node, avanzar y devolver su valor
        if self.current_node is not None:
            value = self.current_node.node_value
            self.current_node = self.current_node.next_node
            return value
        # Si no hay más nodes, lanzar StopIteration
        raise StopIteration