"""
Bloco with: utilziado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.
É a forma pythônica para manipular arquivos
"""

with open('text') as file:
    lines = file.readlines()
    print(file.closed)

print(file.closed)
print(file.closed)
