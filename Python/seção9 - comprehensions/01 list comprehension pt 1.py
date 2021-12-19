"""
Utilizando list comprehension podemos gera novas listas com dados processados
a partir de outro iterável

Sintaxe:
[ dado for in iterable ]

"""

numbers = [1, 2, 3, 4, 5]

result = [number * 10 for number in numbers]
print(result)
print(40 * "=+")

result = [number / 2 for number in numbers]
print(result)
print(40 * "=+")


def power(value):
    return value ** 2


result = [power(number) for number in numbers]
print(result)
print(40 * "=+")
