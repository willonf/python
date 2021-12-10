"""
A função seek() é utilizada para movimentar o cursor no arquivo.
Recebe a posição do cursor como parâmetro.

A função readline() é utilizada para ler uma linha específica.
Por padrão inicial na primeira linha.

Obs.: Quando abrimos um arquivo com a função open() é criada uma conexão entre
o arquivo no disco do computador e o nosso programa. Essa conexão é chamada
de streaming. Depois de finalizado, devemos fechar essa conexão
com a função close()

A propriedade closed verifica se o arquivo estiver aberto ou fechado.
"""

file = open('text', encoding='UTF-8')

print(file.read(), end='\n\n')


file.seek(2)

print(file.read())
print(20*'+=')
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline(5))
file.seek(0)
print(20*'+=')

lines = file.readlines()
print(lines)
print(file.closed)
file.close()
print('Arquivo fechado')
print(file.closed)
