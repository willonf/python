"""
Collections -> High-performance container datetypes

Counter - Recebe um iterável como parâmetro e cria um object do tipo Collections Counter, semelhante
a um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valro a quantidade de
ocorrências desse elemento
"""

# Utilizando o counter

from collections import Counter

lista = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10]

res = Counter(lista)
print(type(res))
print(res)
print(res[8])

print(Counter('Willon Ferreira'))

texto = '''Python é uma linguagem de programação de alto nível,
interpretada de script, imperativa, orientada a objetos, funcional,
de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.
Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado
pela organização sem fins lucrativos Python Software Foundation.
'''

palavras = texto.split()

res = Counter(palavras)
print(res)
print(res.most_common(5))
print(res.most_common(10))
