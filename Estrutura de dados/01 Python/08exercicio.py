alunos = {'Pedro': 8.0,
          'Maria': 10.0,
          'Hamilton': 7.5}

with open('08exercicio.txt', 'w') as text:
    for nome, nota in alunos.items():
        texto = f'Nome: {nome} | Nota: {nota}\n'
        text.write(texto)

with open('08exercicio.txt', 'r') as text:
    for linha in text:
        print(linha, end='')
