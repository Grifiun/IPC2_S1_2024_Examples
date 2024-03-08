class Student:
    def __init__(self, dpi, name, last_name, email, gender, inscrito):
        self.dpi = dpi
        self.name = name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.inscrito = inscrito

    def print_values(self):
        print(f"DPI: {self.dpi}")
        print(f"Nombre: {self.name}")
        print(f"Apellido: {self.last_name}")
        print(f"Correo electrónico: {self.email}")
        print(f"Género: {self.gender}")
        print(f"Inscrito: {self.inscrito}")