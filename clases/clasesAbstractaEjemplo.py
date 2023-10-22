from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nommbre,edad,sexo,actividad):
        self.nombre = nommbre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    

    @abstractclassmethod
    def realizar_actividad(self):
        pass

    # metodo generico

    def presentarse(self):
        print(f"Hola nombre es {self.nombre} y tengo {self.edad} años de edad")


class Estudiante(Persona):
    def __init__(self,nommbre,edad,sexo,actividad):
        super().__init__(nommbre,edad,sexo,actividad)

    def realizar_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


edgar = Estudiante("Edgar",21,"Masculino","programacion Web")

edgar.realizar_actividad()