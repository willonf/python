"""
Reversed: Reverte o iterável. Obs.: Só funciona com iteráveis
"""

lista = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8]
lista.reverse()  # Altera a lista
print(lista)
lista.reverse()  # Altera a lista
result = reversed(lista)
print(type(result))
print(list(result))
print(tuple(reversed(lista)))
print(set(reversed(lista)))

for letter in reversed('WILLON FERREIRA'):
    print(letter, end=' ')
