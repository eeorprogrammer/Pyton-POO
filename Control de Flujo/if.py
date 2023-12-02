# control de flujo

edad = int(input("Que edad tienes ? "))

if (edad < 18):
    print("no puedes ver la pelicula")

elif (edad >= 18 and edad <= 59):
    print("puedes ver la pelicula")

elif edad >= 60:
    print("Puedes ver la pelicula aplicando descuento")


else:
    print("No puedes ver la pelicula")
    print("Ve a otro lado!")


print("Listo!")
