def nums():
    for num in range(1, 11):
        yield num


gen1 = nums()

print(gen1)
print(next(gen1))
print(next(gen1))
print(next(gen1))

# Generator expression

gen2 = (num for num in range(1, 11))
print(gen2)
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(25 * '+=')

import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1, 100000000)))
gen_fim = time.time()
print(f'Tempo: {gen_fim - gen_inicio}')
print(25 * '+=')

# List Comprehension
gen_inicio = time.time()
print(sum([num for num in range(1, 100000000)]))
gen_fim = time.time()
print(f'Tempo: {gen_fim - gen_inicio}')
print(25 * '+=')
