"""
writer

writerow() - escrever uma linha

"""

# from csv import writer
from csv import DictWriter

# with open(file='filmes.csv', mode='w', encoding='utf-8') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
#
#     while filme != 'sair':
#         filme = input('Digite o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Digite o gênero do filme: ')
#             duracao = input('Digite a duração do filme: ')
#             escritor_csv.writerow([filme, genero, duracao])

# Passo 1: Escrevendo o cabeçalho
cabecalho = ['Título', 'Gênero', 'Duração']
with open(file='filmes2.csv', mode='w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()

# Passo 2: escrevendo os filmes. Em caso de adição de novos filmes, chamar apenas o passo 2
with open(file='filmes2.csv', mode='a', encoding='utf-8', newline='') as arquivo:
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    filme = None
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Digite o gênero do filme: ')
            duracao = input('Digite a duração do filme: ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
