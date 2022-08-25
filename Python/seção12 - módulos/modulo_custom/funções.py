def soma(a: int, b: int) -> int:
    return a + b


def soma_2(fn=soma, num=0):
    return num + fn(0, 2)


def numeros(num0=0):
    return num0, 1, 2, 3, 4


def acesso():
    print('Você acessou o módulo')


acesso()

# Trecho de código que será executado quando este módulo
# for executado diretamente

# Quando for importado, __name__ receberá o nome do arquivo (sem extensão)
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(sum(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(sum(tupla))
