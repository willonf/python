total = 0


def increment():
    global total

    total = total + 1
    return total


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador

    print(f'CONTADOR FORA(): {contador}')
    return dentro()


# print(total)
# print(increment())
# print(increment())
# print(total)
print(fora())
print(fora())
