from controller.student_controller import StudentController
from controller.course_controller import CourseController
from xml_service.load_xml_service import LoadXMLService
from xml_service.xml_dom import XMLDom
from xml_service.xml_tree import XMLTree

def load_entity(xml_service, name_entity = ""):
    # Cargar archivo de estudiantes
    xml_loader = LoadXMLService(xml_service)
    xml_element = xml_loader.read_xml()
    if xml_element:
        xml_service.print_xml_node(xml_element)
        return xml_element, xml_loader
    else:
        print(f"No se cargó el archivo de {name_entity}." )
        return None, None

def print_xml_element_list(entity_controller, xml_element_list, name_entity = ""):
    if xml_element_list is None:
        print(f"Cargue primero el archivo de {name_entity}.")
        return

    # Reemplaza print_students con xml_element_to_string
    list_string = entity_controller.xml_element_list_to_string(xml_element_list)
    print(list_string)

def main():
    # Crear una instancia de LoadXMLDom sin proporcionar un path (se usará el FileDialog)
    # Aca pueden comentar y descomentar uno y otro
    # xml_service = XMLDom()
    xml_service = XMLTree()

    # Crear instancia de LoadXMLDom y StudentController, CourseController
    xml_loader_course = None # LoadXMLService(xml_service, None, True)
    xml_loader_student = None # LoadXMLService(xml_service, None, False)

    # Controllers
    student_controller = StudentController(xml_service)
    course_controller = CourseController(xml_service)

    # Son los listados tanto para estudiante como para curso
    xml_element_student_list = None
    xml_element_course_list = None

    while True:
        print("\nMenú:")
        print("1. Cargar estudiantes")
        print("2. Cargar cursos")
        print("3. Ver lista (primeros 10) de alumnos")
        print("4. Ver lista (primeros 10) de cursos")
        print("5. Buscar estudiante por DPI")
        print("6. Buscar cursos por codigo")
        print("7. Guardar datos estudiante")
        print("8. Guardar datos cursos")
        print("9. Salir")

        choice = input("Ingrese el número de la opción deseada: ")

        if choice == "1":
            # Cargar archivo de estudiantes
            xml_element_student_list, xml_loader_student = load_entity(xml_service, "Estudiantes")

        elif choice == "2":
            # Cargar archivo de cursos
            xml_element_course_list, xml_loader_course = load_entity(xml_service, "Cursos")

        elif choice == "3":
            print_xml_element_list(student_controller, xml_element_student_list, "Estudiantes")

        elif choice == "4":
            print_xml_element_list(course_controller, xml_element_course_list, "Cursos")

        elif choice == "5":
            if xml_element_student_list is None:
                print("Cargue primero el archivo de estudiantes.")
                continue  # Volver al menú principal

            dpi = input("Ingrese el dpi del estudiante a buscar: ")
            element_student = student_controller.get_entity_by_id(xml_element_student_list, dpi)

            if element_student is None:
                print("No se encontró al estudiante con el DPI ingresado")
                continue  # Volver al menú principal

            while True:
                print("\n")
                # imprimimos el estudiante con el dpi buscado
                student_controller.xml_element_to_string(element_student)
                print("\nMenú:")
                print("1. Actualizar nombres")
                print("2. Actualizar apellidos")
                print("3. Actualizar email")
                print("4. Actualizar genero")
                print("5. Salir")

                sub_choice = input("Ingrese el número de la opción deseada: ")
                new_value = None

                try:
                    sub_choice = int(sub_choice)
                    if 1 <= sub_choice <= 4:
                        new_value = input("Ingrese el nuevo valor de la opción: ")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

                if sub_choice == 1:
                    student_controller.update_name(element_student, new_value)
                elif sub_choice == 2:
                    student_controller.update_last_name(element_student, new_value)
                elif sub_choice == 3:
                    student_controller.update_email(element_student, new_value)
                elif sub_choice == 4:
                    student_controller.update_gender(element_student, new_value)
                elif sub_choice == 5:
                    break  # Salir del bucle secundario y volver al menú principal
                else:
                    print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

        elif choice == "6":
            if xml_element_course_list is None:
                print("Cargue primero el archivo de cursos.")
                continue

            code = input("Ingrese el código del curso: ")
            element_course = course_controller.get_entity_by_id(xml_element_course_list, code)

            # Si se encontro el curso con code dado seguimos, sino, terminamos esta iteracion y seguimos con otra
            if element_course is None:
                print(f"No se encontró el curso con código {code}")
                continue

            # Menú de cursos
            while True:
                print("Valores del curso")
                course_controller.xml_element_to_string(element_course)

                print("\nMenú de Cursos:")
                print("1. Actualizar nombre del curso")
                print("2. Actualizar valor de créditos")
                print("3. Salir")

                course_option = input("Ingrese el número de la opción deseada: ")

                new_value = None

                try:
                    course_option = int(course_option)
                    if 1 <= course_option <= 2:
                        new_value = input("Ingrese el nuevo valor de la opción: ")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

                if course_option == 1:
                    course_controller.update_attribute_value(element_course, "name", new_value)

                elif course_option == 2:
                    course_controller.update_attribute_value(element_course, "credits_value", new_value)

                elif course_option == 3:
                    break  # Salir del bucle del menú de cursos
                else:
                    print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

        elif choice == "7":
            if xml_element_student_list is None:
                print("Cargue primero el archivo de estudiantes.")
                continue

            xml_loader_student.write_xml(xml_element_student_list)
            print("Datos guardados en 'alumnos.xml'")

        elif choice == "8":
            if xml_element_course_list is None:
                print("Cargue primero el archivo de cursos.")
                continue

            xml_loader_course.write_xml(xml_element_course_list)
            print("Datos guardados en 'cursos.xml'")


        elif choice == "9":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.")


if __name__ == "__main__":
    main()
