"""
Lambdas expressions são funções sem nome, ou seja, funções anônimas
"""


def funcao(a: int):
    return 3 * a + 1



print(funcao(3))

calc = lambda x: 3*x + 1  # Forma não ideal
print(calc(3))


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('willon', 'ferreira'))



hello_world = lambda: "Hello, World!"
print(hello_world())

autores = ['Isaac Asimov', 'Ray Bradburry', 'Robert heinlein', 'Arthur C. Clarke', 'Frank Herbert',
            'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função lambda a*x**2 + b*x + c"""
    return lambda x: a * x ** 2 + b*x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(3,0,1)(2))

