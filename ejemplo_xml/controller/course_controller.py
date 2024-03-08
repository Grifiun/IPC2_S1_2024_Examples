from controller.entity_controller import EntityController
from dao.course import Course


class CourseController(EntityController):
    def __init__(self, xml_service):
        super().__init__(xml_service, "course", "code")

    def xml_element_to_entity(self, xml_element):
        code = int(self.xml_service.get_node_text_by_tag(xml_element, 'code'))
        name = self.xml_service.get_node_text_by_tag(xml_element, 'name')
        credits_value = int(self.xml_service.get_node_text_by_tag(xml_element, 'credits_value'))

        return Course(code, name, credits_value)

    def entity_to_xml_element(self, course):
        # Create the XML element for the course using XMLDom functions
        doc, course_element = self.xml_service.create_xml_node("course")

        # Use the new method to create and append a node with text for each attribute
        self.xml_service.create_and_append_node_with_text_to_node(doc, course_element, "code", str(course.code))
        self.xml_service.create_and_append_node_with_text_to_node(doc, course_element, "name", course.name)
        self.xml_service.create_and_append_node_with_text_to_node(doc, course_element, "credits_value",
                                                                  str(course.credits_value))

        return course_element

    def update_code(self, xml_element, new_code):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "code", str(new_code))

    def update_name(self, xml_element, new_name):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "name", new_name)

    def update_credits_value(self, xml_element, new_credits_value):
        self.xml_service.update_xml_node_value_by_tag(xml_element, "credits_value", str(new_credits_value))
