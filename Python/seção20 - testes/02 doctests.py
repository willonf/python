"""
Doctests são testes que colocamos na docstring das funções
Doctest é reconhecido com '>>>'
Para executar o programa normalmente: python <nome do programa>
Para executar com o doctest incluso: python -m doctest -v <nome do programa>
"""


# def soma(a, b):
#     """
#     Soma os números a e b
#     >>> soma(1, 2)
#     3
#     >>> soma(3,4)
#     5
#     """
#     return a + b


# def duplicar_lista(lista):
#     """
#     >>> duplicar_lista([1,2,3])
#     [2, 4, 6]
#
#     >>> duplicar_lista([])
#     []
#
#     >>> duplicar_lista([True, None])
#     Traceback (most recent call last):
#       ...
#     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#     """
#     return [2 * element for element in lista]


# def falar_oi():
#     """
#     >>> falar_oi()
#     'oi'
#
#     >>> falar_oi()
#     "oi"
#     """
#     return "oi"

def verdade():
    """
    >>> verdade()
    True
    """
    return True
