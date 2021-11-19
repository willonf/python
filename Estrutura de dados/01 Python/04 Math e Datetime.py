import math
from decimal import Decimal, getcontext
print(getcontext())
getcontext().prec = 5
print(getcontext())
print('\nOPERAÇÕES:')
print(f'Raiz quadrada de 9 é igual a: {math.sqrt(9):10.2f}')
print(f'{math.sin(45):5.3f}')
