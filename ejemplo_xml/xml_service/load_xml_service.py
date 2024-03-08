import os
from file.file_dialog import FileDialog


class LoadXMLService:
    def __init__(self, xml_service, path_file=None):
        print("Constructor load XML")
        self.xml_service = xml_service
        if path_file:
            if not os.path.exists(path_file):
                raise FileNotFoundError("El archivo no existe")
            else:
                self.path_file = path_file
        else:
            # Instanciar la clase FileDialog
            file_dialog = FileDialog()

            # Obtener el path seleccionado
            selected_file_path = file_dialog.select_file()

            # Cerrar el selector de archivos después de seleccionar uno
            try:
                file_dialog.root.destroy()
            except AttributeError:
                # Manejar el caso en el que root no está disponible
                pass

            self.path_file = selected_file_path

    def read_and_print_xml(self):
        try:
            self.xml_service.read_and_print_xml(self.path_file)
        except Exception as e:
            print(f"Error al leer el archivo XML: {e}")
        finally:
            print("Se finalizó de leer el archivo xml")
            pass

    def read_xml(self):
        try:
            return self.xml_service.load_xml(self.path_file)
        except Exception as e:
            print(f"Error al leer el archivo XML: {e}")
            return None
        finally:
            print("Se finalizó de leer el archivo xml")
            pass

    def write_xml(self, xml_element):
        try:
            self.xml_service.write_xml(xml_element, self.path_file)
            print(f"Datos guardados en '{self.path_file}'")
        except Exception as e:
            print(f"Error al escribir el archivo XML: {e}")
        finally:
            print("Se finalizó de escribir el archivo XML")


# Verifica si este archivo es el punto de entrada principal
if __name__ == "__main__":
    # Crear una instancia de LoadXMLDom sin proporcionar un path (se usará el FileDialog)
    # xml_service = XMLDom()
    # xml_loader = LoadXMLService(xml_service)

    # Leer el archivo XML
    # xml_loader.read_and_print_xml()
    pass
