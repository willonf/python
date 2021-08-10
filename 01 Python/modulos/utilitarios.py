def soma(a, b, c):
    soma = a + b + c
    return soma


def prod(a, b, c):
    prod = a * b * c
    return prod


def isPalind(texto):
    if texto == texto[::-1]:
        return True
    else:
        return False
