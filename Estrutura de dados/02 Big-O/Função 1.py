import timeit
def soma1(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma

def soma2(n):
    return (n*(n+1)/2)


# soma1() executa 11 passos. Big-O: O(n)
# soma2() executa 3 passos. Big-O: O(n)
a = timeit.default_timer()
soma1(1500)
b = timeit.default_timer()
print(f'Tempo: {(b-a):.10f}')

a = timeit.default_timer()
soma2(1500)
b = timeit.default_timer()
print(f'Tempo: {(b-a):.10f}')

# print(timeit.timeit('''
# def soma1(n):
#     soma = 0
#     for i in range(n+1):
#         soma += i
#     return soma
# soma1(10)
# '''
# ))

# print(timeit.timeit('''
# def soma2(n):
#     return (n*(n+1)/2)
# soma2(10)
# '''
# ))
