# import random
from random import random, uniform, randint, choice, shuffle

# .random() gera um número aleatório entre 0 e 1
# print(random.random())
print(random())

# .uniform() gera um número no intervalo estabelecido
print(uniform(0, 10))

# .randint() gera um numero inteiro aleatório no intervalo estabelecido
print(randint(0, 10))

# .choice() pega um valor aleatório de um iterável
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print(choice('Willon'))

# .shuffle() embaralha os dados
numeros = ['1', '2', '3', '4', '5', '6']
print(numeros)
shuffle(numeros)
print(numeros)
