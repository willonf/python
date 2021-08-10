def mensagem1():
    print('Texto da função')


def mensagem2(texto):
    print(texto)


def soma(a, b):
    print(a+b)


def soma2(a, b):
    return a+b


def calcula_energia(m, h, g=10):
    '''
    Essa função calcula a energia potencial gravitacional
    '''
    energy = m * g * h
    return energy


mensagem1()
mensagem2("Willon Ferreira")
soma(2, 5)
print(soma2(4, -8))
print(help(calcula_energia))
print(calcula_energia(30, 12))
print(calcula_energia(30, 12, 9.8))
