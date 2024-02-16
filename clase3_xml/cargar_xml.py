import tkinter as tk
from tkinter import filedialog
from xml_dom.xml_dom import read_and_print_xml

# Función para manejar el botón de selección de archivo
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
    if file_path:
        read_and_print_xml(file_path)

# Crear la ventana principal
root = tk.Tk()
root.title("Selección de Archivo XML")

# Crear un botón para seleccionar el archivo
select_button = tk.Button(root, text="Seleccionar Archivo", command=select_file)
select_button.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
