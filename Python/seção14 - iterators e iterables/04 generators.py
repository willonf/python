"""
Generators:
    São iterators, mas nem todo iterable é um generator
    Podem ser criados com funções geradoras
    Funções geradoras utilizam o yield
    Podem ser construídos com expressões geradoras
    Possuem um excelente desempenho em memória

Diferenças entre Funções e Generator Functions
    ----------------------|---------------------------
    |    Funções          |    Generator Functions   |
    ----------------------|---------------------------
    Utilizam o return     |    Utilizam yield
    retorna 1 vez         |    Pode utilizar yeild várias vezes
    pode retornar um valor|    Retorna um generator
    ---------------------------------------------------
"""


# Exemplo função geradora
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # Só passa desse ponto com a chamada da
        # função next
        contador = contador + 1


gen = conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(30 * '=+')

gen2 = conta_ate(10)
next(gen2)
for n in gen2:  # Vai começar em 2 e não em 1
    print(n, end=' ')
print(30 * '=+')

gen3 = conta_ate(6)
list_gen = list(gen3)
print(list_gen)
