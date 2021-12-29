"""
Reduce - Importada do módulo 'functools'.
Recebe como parâmetros uma função (com 2 parâmetros) e um iterável
Utilize a função reduce se for realmente necessário. Um loop for é mais legível na maioria dos casos
"""

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]

produto = lambda x, y: x * y  # Aconselhável utilizar declaração def
result = reduce(produto, dados)
print(result)
print(30 * "+=")

result = 1
for number in dados:
    result *= number
print(result)