import timeit


def lista1():
    lista = []
    for i in range(1000):
        lista.append(i)  # ou lista += [i]
    return lista

def lista2():
    return range(1000)


start = timeit.default_timer()
print(lista1())
end = timeit.default_timer()
time1 = end - start

print(30*'+=')

start = timeit.default_timer()
l = lista2()
for i in l:
    print(i, end=' ')
end = timeit.default_timer()
time2 = end - start
print(f'\nTime execution 1: {time1:8f}')
print(f'Time execution 2: {time2:8f}')
