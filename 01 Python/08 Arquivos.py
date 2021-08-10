with open('./texto.txt') as text:
    for linha in text:
        print(linha)

with open('./texto.txt') as text:
    conteudo = text.readlines()
    print(conteudo)

with open('./texto2.txt', 'w') as texto:
    texto.write('Olá a todos! Eu sou o computador do Will.')
