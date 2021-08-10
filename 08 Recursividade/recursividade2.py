import timeit

def sum1(n):
    soma = 0
    for number in range(n+1):
        soma += number
    return soma


def sum2(n):
    if n == 0:
        return 0
    return n + sum2(n-1)


a = timeit.default_timer()
print(sum1(100))
b = timeit.default_timer()
print(f'Tempo a: {(b-a):.10f}', end="\n\n")

a = timeit.default_timer()
print(sum2(100))
b = timeit.default_timer()
print(f'Tempo b: {(b-a):.10f}', end="\n")
