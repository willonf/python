"""
Collection Default Dict
"""

# Dicionário em Python
dicionario = {'curso': 'Python', 'plataforma': 'Udemy'}
print(dicionario)
print(dicionario['curso'])
# print(dicionario['carga'])  # Gera um key error
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
# Default dict
# Não gera key error, pois um valor default é informado, utilizando um lambda.
# Assim, se uma chave for inexistente no dicionário, a chave é criada com o valor padrão

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Python'
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])
print(dicionario.items())
