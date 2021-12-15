"""
Documentação com Docstrings
"""


# Exemplos

def diz_oi():
    """
    Uma função simples que retorna a string 'Oi!'
    """
    return 'Oi!'


def potencia(numero, expoente=2):
    """
    Função que retorna por padrão o quadrado de um número ou um número elevado a uma potência informada.
    :param numero: Base
    :param expoente: Expoente. O padrão é 2
    :return: Retorna 'numero' elevado a 'potencia'
    """
    return numero ** expoente


print(help(diz_oi))
print(50 * "=+")
print(diz_oi.__doc__)
print(50 * "=+")
print(help(potencia))
print(50 * "=+")
print(potencia.__doc__)
