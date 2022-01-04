import primeiro


def message2():
    primeiro.message()


if __name__ == '__main__':
    message2()
    print('segundo.py executado diretamente')
else:
    print(f'segundo.py importado. {__name__}')
