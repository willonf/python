def soma(a: int, b: int) -> int:
    return a + b


def soma_2(fn=soma, num=0):
    return num + fn(0, 2)


def numeros(num0=0):
    return num0, 1, 2, 3, 4


print(soma(5, 7))
print(soma(b=4, a=1))
nums = numeros()
n0, n1, n2, n3, n4 = numeros()
print(nums)
print(n0)
print(n1)
print(n2)
print(soma_2(num=2))
