class Gato:
    def sonido(self):
        return "Miua"


class Perro:
    def sonido(self):
        return "Gua"


def hacer_sonido(animal):
    print(animal.sonido())

garfield = Gato()

hachi = Perro()


hacer_sonido(garfield)