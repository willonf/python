"""
CSV - Comma Separeted Value
"""

# Forma menos usual de trabalho com arquivos .csv
# with open('lutadores.csv', encoding='utf-8') as arquivo:
#     dados = arquivo.read().split('\n')
#     # print(type(dados))
#     print(dados)

# Reader
from csv import reader, DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)  # reader vai retornar um iterator
    next(leitor_csv)  # Pula a primeira linha
    for linha in leitor_csv:
        print(f'Lutador: {linha[0]}\t|\tNascimento : {linha[1]}\t|\tAltura (cm): {linha[2]}')

print(40 * "+=")

# Dict reader
with open('lutadores.csv', encoding='utf-8') as arquivo:
    # DictReader vai retornar um ordered dict. Delimiter é o caractere separador, tendo como padrão a vírgula
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        print(f"Lutador: {linha['Nome']} | Nascimento : {linha['País']} | Altura (cm): {linha['Altura (em cm)']}")
