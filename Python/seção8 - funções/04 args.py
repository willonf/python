"""
*args: Definição padrão, mas pode ser outro nome. Os parâmetros informados na função, são passados como tupla
"""


def print_numeros(*args):
    print(args)


print_numeros(1, 2, 3, 4, 5)
print_numeros((1, 2, 3, 4), 5, 6)
print_numeros([1, 2, 3, 4], 5, 6)

numeros = [1, 2, 3, 4]

# Desempacotamento:
print_numeros(*numeros)
