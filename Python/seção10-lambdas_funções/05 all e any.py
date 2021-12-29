"""
Any e all

all() -> retorna true se todos os elementos do iterável são verdadeiros ou se o iterável está vazio
any() -> retorna true se algum elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna false
"""

print(all([0, 1, 2, 3, 4, 5, 6]))  # False
print(all([1, 2, 3, 4, 5, 6]))
print(all([]))  # Está vazio? True
print(all('Willon'))
print(all({1, 2, 3, 4, 4, 5, 6, 7, 8}))
print(30 * '=+')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all(nome[0] == 'C' for nome in nomes))  # Verificando se TODOS tem a inicial 'C'
print(30 * '=+')
print(30 * '=+')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Willon', 'Naty']
print(any(nome[0] == 'C' for nome in nomes))  # Verificando se ALGUM tem a inicial 'C'
print(any([]))
