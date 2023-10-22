class Auto():

    # construcotor de la clase Auto

    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("conduciendo el automovil")

# creando objetos de la clase

carro = Auto()

carro.conducir()