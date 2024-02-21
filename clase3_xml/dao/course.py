class Course:
    def __init__(self, code, name, credits_value):
        self.code = code
        self.name = name
        self.credits_value = credits_value

    def print_values(self):
        print(f"Codigo: {self.code}")
        print(f"Nombre: {self.name}")
        print(f"Creditos valor: {self.credits_value}")

if __name__ == "__main__":
    course = Course("1", "ej", "0")
    course.print_values()