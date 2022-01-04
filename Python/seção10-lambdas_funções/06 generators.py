"""
Generators
Generator é mais performático que list comprehension.
Ao usar any e all, é recomendável usar generators
"""

from sys import getsizeof

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))  # Any recebe um list comprehension
print(all(nome[0] == 'C' for nome in nomes))  # Any recebe um generator
gen = (nome[0] == 'C' for nome in nomes)  # Generator deve estar entre parenteses
print(type(gen))
print(list(gen))
# Obs.: após utilizarmos o generator ele é zerado.
print(30 * "=+")

# Getsizeof retorna a quantidade de bytes em memória
print(getsizeof('Geek'))
print(getsizeof(nome[0] == 'C' for nome in nomes))
print(getsizeof([nome[0] == 'C' for nome in nomes]))
print(30 * "=+")

# List comprehension
print(getsizeof([x * 10 for x in range(1000)]))

# Set comprehension
print(getsizeof({x * 10 for x in range(1000)}))

# Dict comprehension
print(getsizeof({x: x * 10 for x in range(1000)}))

# Generator expression
print(getsizeof(x * 10 for x in range(1000)))
print(30 * "=+")

# É possível iterar no generator

gen = (x for x in range(10))

for number in gen:
    print(number, end=' ')
