# ejercicio funciones - palindromos

def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()

# comparamos el texto original con su version invertida
    return texto == texto[::-1]


print("Abba", es_palindromo("Abba"))
print("anita lava la tina", es_palindromo("anita lava la tina"))
print("Reconocer", es_palindromo("Reconocer"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("amo la paloma", es_palindromo("amo la paloma"))
print("hola como estas", es_palindromo("hola como estas"))
