from controller.entity_controller import EntityController
from dao.student import Student


class StudentController(EntityController):
    def __init__(self, xml_service):
        super().__init__(xml_service, "student", "dpi")

    def xml_element_to_entity(self, xml_element):
        dpi = int(self.xml_service.get_node_text_by_tag(xml_element, 'dpi'))
        name = self.xml_service.get_node_text_by_tag(xml_element, 'name')
        last_name = self.xml_service.get_node_text_by_tag(xml_element, 'last_name')
        email = self.xml_service.get_node_text_by_tag(xml_element, 'email')
        gender = self.xml_service.get_node_text_by_tag(xml_element, 'gender')
        inscrito = self.xml_service.get_node_text_by_tag(xml_element, 'inscrito').lower() == "true"

        return Student(dpi, name, last_name, email, gender, inscrito)

    def entity_to_xml_element(self, student):
        # Create the XML element for the student using XMLDom functions
        doc, student_element = self.xml_service.create_xml_node("student")

        # Use the new method to create and append a node with text for each attribute
        self.xml_service.create_and_append_node_with_text_to_node(doc, student_element, "dpi", str(student.dpi))
        self.xml_service.create_and_append_node_with_text_to_node(doc, student_element, "name", student.name)
        self.xml_service.create_and_append_node_with_text_to_node(doc, student_element, "last_name", student.last_name)
        self.xml_service.create_and_append_node_with_text_to_node(doc, student_element, "email", student.email)
        self.xml_service.create_and_append_node_with_text_to_node(doc, student_element, "gender", student.gender)
        self.xml_service.create_and_append_node_with_text_to_node(doc, student_element, "inscrito",
                                                                  str(student.inscrito))

        return student_element

    """
    Este codigo se movio para entity_controller.py
    Se deja aca como evidencia de que se puede modularizar SIEMPRE
    --------------------------------------------------------------------
    
    def xml_element_list_to_string(self, xml_elements):
        # Llamando a la implementación de la clase base
        return super().xml_element_list_to_string(xml_elements)

    
    def xml_element_list_to_string(self, xml_element):
        # Imprimir los primeros 10 elementos (puedes ajustar según sea necesario)

        for student_node in self.xml_service.get_xml_node_list_by_tag(xml_element, "student")[:10]:
            student_entity = self.xml_element_to_entity(student_node)
            student_entity.print_values()
            print("\n")

        # Retornar una cadena informativa (puedes personalizar según tus necesidades)
        return "Primeros 10 elementos impresos."

    def xml_element_to_string(self, xml_element):
        if xml_element:
            student_entity = self.xml_element_to_entity(xml_element)
            student_entity.print_values()
    """

    """
    def get_student_by_dpi(self, xml_element, dpi):
        # XML element contendrá el listado total de estudiantes
        if xml_element:
            # Buscar elemento por DPI
            student_nodes = self.xml_service.get_xml_node_list_by_tag(xml_element, "student")

            for student_node in student_nodes:
                student_node_text = self.xml_service.get_node_text_by_tag(student_node, "dpi")
                print("Text: {} vs {}".format(student_node_text, dpi))
                if student_node_text == dpi:
                    return student_node

        # Retornar None si no se encuentra el estudiante con el DPI dado
        return None"""

    def update_dpi(self, xml_element, new_dpi):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "dpi", new_dpi)

    def update_name(self, xml_element, new_name):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "name", new_name)

    def update_last_name(self, xml_element, new_last_name):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "last_name", new_last_name)

    def update_email(self, xml_element, new_email):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "email", new_email)

    def update_gender(self, xml_element, new_gender):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "gender", new_gender)

    def update_inscrito(self, xml_element, new_inscrito):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "inscrito", new_inscrito)
