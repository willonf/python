"""
Decorators (decoradores):
    São funções
    Envolvem outras funções e aprimoram seu comportamento
    Geralmente recebem uma função como parâmetro

Exemplo de sintaxe:
    def <nome da decorator function>(funcao):
        def <função interna>:
            instruções
            funcao()
        return <funcao interna>
"""


# Função decorator
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você.')
        funcao()
        print('Tenha um otimo dia!')

    return sendo


def saudacao():
    print('Seja bem-vindo à Terra.')


teste = seja_educado(saudacao)
teste()
print(30 * '=+')


# Decorators com Syntax Sugar (Açúcar sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você.')
        funcao()
        print('Tenha um otimo dia!')

    return sendo_mesmo


def oi(funcao):
    def print_oi():
        print('Oi')
        funcao()

    return print_oi


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Nolliw')


@oi
def apresentando2():
    print('Meu nome é Willon')


apresentando()
print(30 * '=+')
apresentando2()
