class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

 
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre


edgar = Persona("Edgar",21)

nombre= edgar.set_nombre("Emilio")

print(nombre)