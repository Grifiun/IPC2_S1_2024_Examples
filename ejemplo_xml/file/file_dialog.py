import tkinter as tk
from tkinter import filedialog

class FileDialog:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Selección de Archivo XML")

        # Crear un botón para seleccionar el archivo
        self.select_button = tk.Button(self.root, text="Seleccionar Archivo", command=self.select_file)
        self.select_button.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
        return file_path

    def run(self):
        # Iniciar el bucle principal de la interfaz gráfica
        self.root.mainloop()

# Si ejecutas este archivo directamente, ejecuta la interfaz gráfica
if __name__ == "__main__":
    file_dialog = FileDialog()
    file_dialog.run()
