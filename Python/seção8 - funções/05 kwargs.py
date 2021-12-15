"""
**kwargs: Key args
"""


def cores_favoritas(**kwargs):
    # kwargs se torna um dicionário
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs['will'])


def cores_favoritas2(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'{pessoa}: {cor}')


def cores_favoritas3(**kwargs):
    for key in kwargs:
        print(kwargs[key])


def operacao(a, b, **kwargs):
    if kwargs['op'] == '+':
        return a + b
    elif kwargs['other'] == '-':
        return a - b
    else:
        return a * b


# cores_favoritas(will='azul', lilly='preto', naty='vermelho')
# cores_favoritas2(will='azul', lilly='preto', naty='vermelho')
cores_favoritas3(will='azul', lilly='preto', naty='vermelho')

d = dict(will='azul', lilly='preto', naty='vermelho')

# Desempacotamento
cores_favoritas3(**d)
print(operacao(2, 3, **{'other': '-'}, op='+'))
print(operacao(2, 3, **{'other': '*'}, op='='))
print(operacao(2, 3, **{'other': '-'}, op='='))
