# bucle for en python

# lista de nombres

nombres = ["Edgar","Emilio","Vanessa"]
print("El tipo de nombres es",type(nombres))

for nombre in nombres:
    print("Que pedo",nombre)


# tupla de nombres
nombres = ("Edgar","Emilio","Vanessa")

print("El tipo de nombres es",type(nombres))

for nombre in nombres:
    print("Que pedo",nombre)



# set de nombres

nombres = {"Edgar","Emilio","Vanessa"}

print("El tipo de nombres es",type(nombres))

for nombre in nombres:
    print("Que pedo",nombre)


# diccionario de nombres

nombres = {
    "Edgar":1,
    "Emilio":2,
    "Vanessa":3

}
print("El tipo de nombres es",type(nombres))

for nombre in nombres.items():
    print("Que pedo",nombre)
