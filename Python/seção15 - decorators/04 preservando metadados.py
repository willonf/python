"""
Preservando metadados com wraps
Metadados -> arquivos intrísecos em arquivos

wraps -> funções que envolvem elementos com diversas finalidades
"""

# Problema

# def ver_log(funcao):
#     def logar(*args, **kwargs):
#         """Eu sou uma função (logar) dentro de outra"""
#         print(f'Aqui você está chamando: {funcao.__name__}')
#         print(f'Aqui a documentação: {funcao.__doc__}')
#         return funcao(*args, **kwargs)
#
#     return logar
#
#
# @ver_log
# def soma(a, b):
#     """Soma dois numeros"""
#     return a + b
#
#
# # print(soma(10, 20))
# print(soma.__name__)  # Retorna o nome da função do decorator
# print(soma.__doc__)  # Retorna o docstring do decorator


# Resolução

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # Vai preservar os metadados da função decorada
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Aqui você está chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)

    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma.__name__)
print(soma.__doc__)
