def message():
    print('Olá, tudo bem?')


if __name__ == '__main__':
    message()
    print('primeiro.py executado diretamente')
else:
    print(f'primeiro.py importado. {__name__}')
