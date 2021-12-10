"""
Ordered dict: em um dicionário a ordem de inserção dos elementos não é garantida.
Em um ordered dict a ordem é garantida.
"""

from collections import OrderedDict

non_ordered1 = {'c': 3, 'b': 2, 'a': 1, 'd': 4}
non_ordered2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
ordered = OrderedDict({'c': 3, 'b': 2, 'a': 1, 'd': 4})
# non_ordered1 e non_ordered2 não são Ordered dicts, portanto são iguais.
# Isso muda no caso de "ordered", pois o mesmo é um ordered dict.
for key, value in ordered.items():
    print(f'chave = {key} ---> valor:{value}')
