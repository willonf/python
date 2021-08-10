try:
    n = int(input("Digite um número inteiro:"))
except Exception:
    print('Valor inválido:')
else:
    print(f'O valor digitado é {n}')


while True:
    try:
        t = int(input('Digite um número inteiro: \n'))
    except ValueError:
        print('Valor inválido!')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'Valor digitado: {t}')
        break
