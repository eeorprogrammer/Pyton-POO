tienes_llave = input("¿tienes una llave ? ")

if tienes_llave == "si":
    forma = input("¿Que forma tiene la llave?")
    color = input("¿Que color tiene la llave?")
    if forma == "cuadrada" and color == "naranja":
        print("Entra por la puerta 1")

    elif forma == "redonda" and color == "amarillo":
        print("Entra por la puerta 2")
    
    elif forma == "triangular" and color == "rojo":
        print("Entra por la puerta 3")
    else:
        print("La forma de la llave y el color de la puerta son incorrectos para entrar por alguna de las tres puertas")

else: 
    print("Tienes la llave incorrecta ")



