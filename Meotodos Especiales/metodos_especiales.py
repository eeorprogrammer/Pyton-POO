class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre = {self.nombre},edad = {self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    

Edgar = Persona("Edgar",21)
Emilio = Persona("Emilio",40)
Vanessa = Persona("Vanessa",27)

nueva_persona = Edgar+Emilio+Vanessa
print(nueva_persona)


print(nueva_persona.nombre)