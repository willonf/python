"""
max(): retorna o maior valor de um iterável (tuples, lists, dicts) ou o maior de dois ou mais elementos
"""

lista = [1, 2, 3, 10, 9, 8, 7, 6, 4, 5]
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(max(lista))
print(max(dicionario))  # Maior chave
print(max(dicionario.values()))  # Maior valor

print(max(34, 3))
print(max(34, 3, -5, 90))
print(max('a', 'ab', 'b', 'abc'))
print(max('Willon Ferreira da Silva'))

print(30 * '+=')

print(min(lista))
print(min(dicionario))  # Maior chave
print(min(dicionario.values()))  # Maior valor

print(min(34, 3))
print(min(34, 3, -5, 90))
print(min('a', 'ab', 'b', 'abc'))
print(min('Willon Ferreira da Silva'))
print(30 * '+=')

nomes = ['Arya', 'Samsom', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
print(30 * '+=')

musicas = [
    {'titulo': "Thunderstruck", 'tocou': 3},
    {'titulo': "Back in Black", 'tocou': 5},
    {'titulo': "Highway to hell", 'tocou': 2},
    {'titulo': "Too old to rock'n'roll", 'tocou': 1},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(f"Música mais tocada: {max(musicas, key=lambda musica: musica['tocou'])['titulo']}")
print(min(musicas, key=lambda musica: musica['tocou']))
print(f"Música menos tocada: {min(musicas, key=lambda musica: musica['tocou'])['titulo']}")
