def fat(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fat(n-1)


print(fat(5))