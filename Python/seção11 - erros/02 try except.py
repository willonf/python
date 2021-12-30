"""
Try/excepet: Utilizado para tratar o erro

Sintaxe:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

"""

# Tratando um erro genérico
# try:
#     geek()
# except:
#     print('Algum problema ocorreu na execução da função')


# Tratando um erro específico
# try:
#     geek()
# except NameError:
#     print('Função indefinida')


# try:
#     len(3)
# except TypeError as err:
#     print('Ocorreu um erro:', end=' ')
#     print(err)

# Tratando diferentes tipos de erro
# try:
#     # geek()
#     # len(5)
#     # print('Geek'[9])
# except NameError as err:
#     print('Ocorreu um erro:', end=' ')
#     print(err)
# except TypeError as err:
#     print('Ocorreu um erro:', end=' ')
#     print(err)
# except:
#     print('Um erro diferente ocorreu')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except (KeyError, TypeError) as err:
        return f'Ocorreu um erro: {err}'
    # except TypeError:
    #     return None

dic = {'nome': 'Will'}
print(pega_valor(dic, 'nome'))
print(pega_valor(1, 'name'))
