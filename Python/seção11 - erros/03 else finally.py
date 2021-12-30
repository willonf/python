"""
Try / Except / Else / Finally

Qualquer input no sistema deve ser tratado

O finally geralmente é usado para fechar ou desalocar recursos

"""


# number = None
# try:
#     number = int(input('Informe um número: '))
# except ValueError as err:
#     print('Tipo de valor incorreto')
# else:  # Se não causar exceção, entra no else
#     print(f'Você digitou o valor {number}')


# number = None
# try:
#     number = int(input('Informe um número: '))
# except ValueError as err:
#     print('Tipo de valor incorreto')
# else:
#     print(f'Você digitou o valor {number}')
# finally:  # Executa independente de ter caído no else ou no finally
#     print('Executando o finally')


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
       return f'Ocorreu um erro: {err}'
    except TypeError:
        return 'Tipo de argumento incorreto'


num1 = 4
num2 = 'a'
print(dividir(num1, num2))
