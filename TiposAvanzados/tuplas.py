numeros = (1, 2, 3)+(4, 5, 6)

print(numeros)


punto = tuple([1, 2])
print(punto)

menos_numeros = punto[:2]
print(menos_numeros)


primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)
