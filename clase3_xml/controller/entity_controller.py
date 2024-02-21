from abc import ABC, abstractmethod


class EntityController(ABC):
    def __init__(self, xml_service, entity_tag, id_tag):
        # Aca se puede cambiar a XML_Tree
        self.xml_service = xml_service
        self.entity_tag = entity_tag
        self.id_tag = id_tag

    @abstractmethod
    def entity_to_xml_element(self, entity):
        pass

    @abstractmethod
    def xml_element_to_entity(self, xml_element):
        pass

    # @abstractmethod
    def xml_element_list_to_string(self, xml_elements):
        # Imprimir los primeros 10 elementos (puedes ajustar según sea necesario)
        # [:10] indica que inicia desde la primera posicion entrada y finaliza en posicion 10
        # [0:2] inicia en la pos 0 y finaliza en 2, es decir 3 elements
        # [:] inicia en la pos 0 y finaliza en 2, es decir 3 elements

        for xml_element in self.xml_service.get_xml_node_list_by_tag(xml_elements, self.entity_tag)[:10]:
            self.xml_element_to_string(xml_element)

        # Retornar una cadena informativa (puedes personalizar según tus necesidades)
        return "Primeros 10 elementos impresos."

    # @abstractmethod
    def xml_element_to_string(self, xml_element):
        if xml_element:
            entity = self.xml_element_to_entity(xml_element)
            entity.print_values()
            print("\n")
        pass

    def get_entity_by_id(self, xml_element, entity_id):
        # XML element contendrá el listado total de entidades
        if xml_element:
            # Buscar elemento por el id
            entity_nodes = self.xml_service.get_xml_node_list_by_tag(xml_element, self.entity_tag)

            for entity in entity_nodes:
                entity_text = self.xml_service.get_node_text_by_tag(entity, self.id_tag)
                # print("Text: {} vs {}".format(entity_node_text, entity_id))
                if entity_text == entity_id:
                    return entity

        # Retornar None si no se encuentra el estudiante con el DPI dado
        return None

    def update_attribute_value(self, xml_element, attribute_name, attribute_value):
        if xml_element:
            self.xml_service.update_xml_node_value_by_tag(xml_element, attribute_name, attribute_value)
        else:
            print("XML Element invalido para actualizar")