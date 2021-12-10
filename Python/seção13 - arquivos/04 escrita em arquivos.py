"""
Não é possível realizar escrita em um arquivo aberto no modo leitura e vice-versa

Ao abrir um  arquivo para escrita, o arquivo é criado no sistema operacional
"""

# with open(file='text2', encoding='UTF-8', mode='w') as file:
#     file.write('Escrevendo novo conteúdo no 2º arquivo')
#
# with open(file='text2', encoding='UTF-8', mode='r') as file:
#     print(file.readlines())

print(50 * '+=')

with open(file='text', encoding='UTF-8', mode='a') as file:
    file.write('Última atualização')

with open(file='text', encoding='UTF-8', mode='r') as file:
    lines = file.readlines()
    print(lines)
