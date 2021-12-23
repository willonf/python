"""
Set comprehension
"""

numeros = {num for num in range(1,8)}
print(numeros)


numeros = {x ** 2 for x in range(0,10)}
print(numeros)

letras = {letra for letra in 'AAAEEEIIIOOOUUUaaaeeeiiiooouuu'}
print(letras)
