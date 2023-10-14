class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"

    def _hablar(self):
        print("Hola , como estas")


miObjeto = MiClase()

print(miObjeto._hablar())