"""
Named tuples: são tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros
"""

from collections import namedtuple

# Formas de declaração
Named1 = namedtuple('pets', 'especie idade nome')
Named2 = namedtuple('pets', ['especie', 'idade', 'nome'])
Named3 = namedtuple('pets', 'especie, idade, nome')

pet1 = Named1(nome='Lily', especie='cachorro', idade=1)
print(pet1)
print(pet1.idade)
print(pet1.nome)
print(pet1.especie)
print(f'{pet1[0]} {pet1[1]} {pet1[2]}')
