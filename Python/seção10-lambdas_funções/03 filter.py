"""
Filter - Usado para filtrar dados de uma determinada coleção
Recebe uma função e um iterável como parâmetros
"""
import itertools

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = sum(dados) / len(dados)
print(media)
print(30 * "+=")

# Filtrando valores acima da média
res = filter(lambda x: x > media, dados)
print(res)
print(type(res))
print(list(res))
print(30 * "+=")

# Filtrando valores abaixo da média
res = filter(lambda x: x < media, dados)
print(list(res))
# Obs.: após utilizarmos a função filter() depois da primeira utilização do resultado, ele é zerado.
print(list(res))
print(30 * "+=")

paises = ['', 'Brasil', 'Argentina', '', '', 'Chile', 'Inglaterra', 'Chile', 'Equador']
print(paises)
print(30 * "+=")
res = filter(None, paises)
print(list(res))
print(30 * "+=")

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrando pessoas sem tweets
result = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
result1 = list(filter(lambda user: not user['tweets'], usuarios))
# Filtrando pessoas com tweets
result2 = list(itertools.filterfalse(lambda user: len(user['tweets']) == 0, usuarios))
result3 = list(filter(lambda user: len(user['tweets']), usuarios))
print(result)
print(result1)
print(result2)
print(result3)
print(30 * "+=")

# Combinando map e filter

nomes = ['Vanessa', 'Ana', 'Maria', 'Jo', 'Bia', 'Larissa']
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
