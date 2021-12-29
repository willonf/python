"""
Map - usado para mapeamento de valores para função
"""

import math


def area(r: int):
    """
    Calcula a área de um círculo de raio 'r'
    """
    return math.pi * (r ** 2)


print(area(2))
print('+=' * 30)

# Usando map
areas = map(area, [1, 2, 3, 4])
print(areas)
print(list(areas))  # 1ª utilização
print('+=' * 30)

# Usando map com lambda expression
print(list(map(lambda r: math.pi * (r ** 2), [1, 2, 3, 4])))
print(list(areas))  # 2ª utilização
print(list(areas))  # 3ª utilização
# Obs.: após utilizarmos a função map() depois da primeira utilização do resultado, ele é zerado.
