"""
Módulos built-in são módulos integrados no Python
"""
import builtins
import random as rdm
from random import randint as rdi, shuffle as shf

# Forma pythonica de importar diversos módulos
from random import (
    random,
    randint,
    shuffle,
    randbytes
)

# print(dir(builtins))

print(rdm.random())

numeros = ['1', '2', '3', '4', '5', '6']
print(numeros)
shf(numeros)
print(numeros)


