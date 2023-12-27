'''
Calculadora interactiva
- verificar si el usuario a ingresado un numero anteriormente , si no ha ingresado algun numero indicarle al usuario ke ingrese primero un numero
- si el usuario ya ha ingresado un numero le pedimos ke ingrese una operacion(op)
- despues de ingresar la operacion indicarle al usuario ke ingrese otro numero
- mostrar resultados
'''

print("Bienvenidos a la Calculadora")
print("Para salir escribe salir")
print("Las operaciones son: suma, multi, div, resta")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingresar numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    op = input("Ingresa una operacion: ")
    if op.lower() == "salir":
        break

    n2 = input("Ingresa el siguiente numero: ")
    if n2.lower() == "salir":
        break

    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es: {resultado} ")
