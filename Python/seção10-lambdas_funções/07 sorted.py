"""
Sorted - ordena o iterável sem alterá-lo
"""

lista = [1, 4, 3, 2, 6, 7, 5]
lista.sort()
print(lista)
print(30 * "=+")

lista = [1, 4, 3, 2, 6, 7, 5]
tupla = (1, 4, 3, 2, 6, 7, 5)
print(sorted(lista))
print(lista)
print(sorted(tupla))
print(tupla)
print(30 * "=+")

print(sorted(lista, reverse=True))
print(30 * "=+")

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Em caso de dicionários, é necessário indicar a chave usada como parâmetro de ordenação
print(sorted(usuarios, key=len))
print(sorted(usuarios, key=lambda usuario: usuario['username']))
