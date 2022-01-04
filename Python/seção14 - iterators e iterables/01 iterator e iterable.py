"""
Iterator:
    Objeto que pode ser iterado
    Retorna um dado por vez na chamada do método `next`

Iterable:
    Objeto que vai retornar um iterator na chamada da função `iter`
"""

# Exemplos de iterable: lists, tuples, dicts, sets
nome = 'Geek'
numeros = [1, 2, 3, 4, 5]

# Transformando os iterables em iterators
it1 = nome.__iter__()
it2 = iter(numeros)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it2))
print(next(it2))
print(next(it2))

# O laço for transforma o iterable em iterator
# para iterar em cima dele
for letra in nome:
    print(f'{letra}', end=' ')
