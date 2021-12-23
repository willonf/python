"""
Dictionary Comprehensions

Sintaxe:
{chave: valor for valor in iterável}

"""

numeros = {'a':1, 'b': 2, 'c': 3, 'd':4, 'e':5}
numeros2 = [1,2,3,4]

quadrado = {chave:valor**2 for chave, valor in numeros.items()}
quadrado2 = {valor:valor**2 for valor in numeros2}
print(quadrado)
print(quadrado2)

 # Obs.: não há repetição de chaves

numeros = [1,2,3,4,1,2]
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)

chaves = 'abcde'
valores = [1,2,3,4,5]

mix = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mix)

result = {num: ('par' if num % 2 == 0 else 'ímpar') for num in valores}
print(result)
