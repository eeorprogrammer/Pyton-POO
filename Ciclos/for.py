# el for se puede usar para iterara o recorrer una lista de elementos
# buscar elementos , usar operaciones aritmeticas
buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Numero Encontrado:", buscar)
        break
else:
    print("No se encontro el numero buscado ):")


for char in "Ultimate Python":
    print(char)
