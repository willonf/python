"""
Zip(): Cria um iterável que agrega elementos de cada um dos iteráveis passados como entrada, em pares
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(type(zip1))
print(list(zip(lista1, lista2)))
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))
print(dict(zip1))
print(set(zip(lista1, lista2, 'abcd')))

tupla = 1, 2, 3, 4, 5, 6
lista = [7, 8, 9, 10, 11, 12]
dicionario = {'x': 1, 'y': 2, 'z': 3}

print(list(zip(tupla, lista, dicionario)))

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
