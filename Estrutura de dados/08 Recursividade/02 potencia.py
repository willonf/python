def pot(base, exp):
    if not exp:
        return 1
    else:
        result = base*pot(base, exp - 1)
        return result


print(pot(2, 4))
