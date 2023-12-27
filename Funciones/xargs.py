def suma(*numeros):
    resultado = 0

    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 45, 67, 33)
suma(2, 5, 44, 55, 112, 34, 556, 899)
