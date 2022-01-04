valor = '67.3'


# O parâmetro x em `float` é um parâmetro somente posicional
# print(float(valor))
#
#
# def cumprimenta_v1(nome):
#     return f'Olá, {nome}!'
#
#
# # Tudo que vem ANTES da barra, é parametro posicional
# # Parâmetro posicional é o oposto de parâmetro nomeado
# def cumprimenta_v2(nome, /, sobrenome):
#     return f'Olá, {nome} {sobrenome}!'
#
#
# print(cumprimenta_v1('Willon'))
# print(cumprimenta_v1(nome='Willon'))
# print(cumprimenta_v2('Naty', sobrenome='Sidou'))
# print(cumprimenta_v2('Sidou', sobrenome='Naty'))
# print(cumprimenta_v2('Sidou', 'Naty'))
#
#
# # print(cumprimenta_v2(nome='Naty'))
#
#
# # Parâmetro nomeado "obrigatório"
# APÓS o asterisco, o parâmetro deve ser nomeado obrigatoriamente
def cumprimenta_v3(nome, *, sobrenome):
    return f'Olá, {nome} {sobrenome}!'


print(cumprimenta_v3('Willon', sobrenome='Ferreira'))
print(cumprimenta_v3('Nolliw', sobrenome='Silva'))


def cumprimenta_v4(nome, /, *, sobrenome):
    return f'Olá, {nome} {sobrenome}!'


print(cumprimenta_v3('Willon', sobrenome='Ferreira'))
print(cumprimenta_v3('Nolliw', sobrenome='Silva'))
# print(cumprimenta_v3(sobrenome='Silva', 'Nolliw'))
