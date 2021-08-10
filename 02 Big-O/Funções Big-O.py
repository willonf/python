def constant(n):
    print(n[0])


def linear(n):
    for i in n:
        print(i)


def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)


def combination(n):
    # Big-O(1)
    print(n[0])

    # Big-O(5)
    for i in range(5):
        print('test ', i)

    # Big-O(n)
    for i in n:
        print(i)

    # Big-O(n)
    for i in n:
        print(i)

    # Big-O(3)
    print('Python')
    print('Python')
    print('Python')
# Big-O = O(1) + O(5) + O(n) + O(n) + O(3) = O(9) + O(2n) = O(n)


lista = [1, 2, 3, 4]

constant(lista)
print(30*'+=')

linear(lista)
print(30*'+=')

quadratic(lista)
print(30*'+=')

combination(lista)
print(30*'+=')
