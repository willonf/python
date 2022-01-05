"""
Decorators com diferentes assinaturas
Para resolver esse problema, utilizamos o Decorator Pattern]
--------
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá. Eu me chamo {nome}'


@gritar
def ordernar(principal, acompanhamento):
    return f'Vou querer {principal} e {acompanhamento}'


print(saudacao('Willon'))
print(ordernar('churrasco', 'batata'))

"""


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá. Eu me chamo {nome}'


@gritar
def ordernar(principal, acompanhamento):
    return f'Vou querer {principal} e {acompanhamento}'


print(saudacao('Willon'))
print(ordernar('churrasco', 'batata'))
print(30 * '=+')


# Decorators com argumentos

def verifica_primeiro_argumento(valor):  # Recebe os argumentos do decorator
    def interna(funcao):  # Recebe o nome da função
        def outra(*args, **kwargs):  # Recebe os argumentos da função
            if args and args[0] != valor:
                return f'O 1º argumento precisa ser {valor}'
            return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)  # O parâmetro `valor` vai receber 10 como argumento
def soma_dez(num1, num2):  # o parâmetro `funcao` vai receber soma_dez como argumento
    return num1 + num2


print(soma_dez(10, 12))
print(soma_dez(9, 12))
comida_favorita('pizza', 'churrasco')
comida_favorita('churrasco', 'pizza')
print(30 * '=+')


def decorator_v1(valor):  # Recebe os argumentos do decorator
    print(f'Argumento do decorator: {valor}')

    def interna(funcao):  # Recebe o nome da função
        print(f'Argumento função: {funcao}')

        def outra(*args, **kwargs):  # Recebe os argumentos de `funcao`
            if args:
                return f'Argumento *args: {args}'
            if kwargs:
                return f'Argumento **kwargs: {kwargs}'

        return outra

    return interna


@decorator_v1('A')
def minha_funcao(letra):
    print('C')


print(minha_funcao('B'))
