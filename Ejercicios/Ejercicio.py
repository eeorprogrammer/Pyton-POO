class Persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")


# creando un objeto de la clase estudiante

edgar = Estudiante("Edgar",40,"primer grado")

edgar.mostrar_datos()
edgar.mostrar_grado()