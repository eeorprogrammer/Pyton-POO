class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza},Velocidad: {self.velocidad})"

    def __add__(self,otro_objeto):
        nuevo_nombre = self.nombre + "-" + otro_objeto.nombre
        nueva_fuerza = ((self.fuerza + otro_objeto.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_objeto.velocidad)/2)**2
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)

# creando un objeto de la clase Personaje

Goku = Personaje("Goku",100,100)
Vegeta = Personaje("Vegeta",99,99)

gogeta = Goku + Vegeta


print(gogeta)


