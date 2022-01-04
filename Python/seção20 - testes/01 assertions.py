# Cuidado com o assert: se o programa python for executado
# com o parâmetro -O, nenhum assertion será validado.

def soma_num_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b


# ret = soma_num_positivos(2, 4)
# print(ret)
# ret = soma_num_positivos(-2, 4)
# print(ret)


def comer_fast_food(comida):
    assert comida in ['pizza', 'sorvete', 'hamburguer', 'batata frita'], 'Precisa ser um fast food'
    return f'Estou comendo comida'


comida1 = 'churrasco'
comida2 = 'pizza'
print(comer_fast_food(comida1))
