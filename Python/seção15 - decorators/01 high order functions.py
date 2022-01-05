"""
High order functions = Funções de maior grandeza ou First Class Citizen
Funções que podem retornar outras funções ou usá-las como parâmetros.
"""


def somar(a, b):
    return a + b


def produto(a, b):
    return a * b


def calcular(a, b, funcao):
    return funcao(a, b)


print(calcular(4, 3, somar))
print(calcular(2, 3, produto))

"""
Nested functions ou Inner functions: funções dentro de funções (funções internas)
"""

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Vai embora ', 'Bom dia '))

    return humor() + pessoa


print(cumprimento('Willon'))
print(cumprimento('Nolliw'))
print(cumprimento('Nolliw'))

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('kkk', 'hahahah', 'lololololo'))

    return rir


rindo = faz_me_rir()
print(rindo())
print(rindo())
