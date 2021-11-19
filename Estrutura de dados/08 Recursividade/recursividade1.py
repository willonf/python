def recursao(times):
    print('Recursão')
    times += 1
    if times == 5:
        return
    else:
        recursao(times)


recursao(0)
