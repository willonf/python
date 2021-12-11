"""
StringIO: Utilizado para ler e criar arquivos em memória
"""

from io import StringIO

mensagem = 'Está é apenas uma string normal'

file = StringIO(mensagem)
# Equivalente:
# arquivo = open('arquivo.txt', 'w')

print(file.read())
file.write('\nOutro texto')

file.seek(0)
print(file.read())
