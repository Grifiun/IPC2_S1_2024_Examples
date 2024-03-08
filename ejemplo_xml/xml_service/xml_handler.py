from abc import ABC, abstractmethod


class XMLHandler(ABC):
    @abstractmethod
    def create_xml_node(self, name):
        pass

    @abstractmethod
    def write_xml(self, doc, file_path):
        pass

    @abstractmethod
    def load_xml(self, file_path):
        pass

    @abstractmethod
    def add_child_to_node(self, parent_doc, parent_node, child):
        pass

    @abstractmethod
    def add_text_to_node(self, parent_doc, parent_node, text):
        pass

    @abstractmethod
    def create_and_append_node_with_text_to_node(self, parent_doc, parent_node, name, text):
        pass

    @abstractmethod
    def print_xml_node(self, node, indent=""):
        pass

    @abstractmethod
    def get_node_text(self, node):
        pass

    @abstractmethod
    def get_node_text_by_tag(self, node, tag_name):
        pass

    @abstractmethod
    def read_and_print_xml(self, file_path):
        pass

    @abstractmethod
    def modify_node_text(self, node, new_text):
        pass

    @abstractmethod
    def get_xml_node_by_tag(self, root_node, tag_name):
        pass

    @abstractmethod
    def get_xml_node_list_by_tag(self, root_node, tag_name):
        pass

    @abstractmethod
    def update_xml_node_value_by_tag(self, root_node, tag_name, new_value):
        pass
