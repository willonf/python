# Write an algorithm that takes an array of numbers as input
# and calculates the sum of those numbers.
# Define the Time Complexity of that algorithm
# and determine what the lowest possible Time Complexity is for this problem.

import timeit


def sumNumbers1(lista):
    sum = 0  # O(1)
    for i in lista:  # O(1), only one execution
        sum += i  # O(n)
    return sum  # O(1)
# T = 1 + 1 + n + 1 = 3 + 1*n = n => O(n) Linear Time Complexity


lista = [1, 2, 3, 4, 5]
start = timeit.default_timer()
print(sumNumbers1(lista))
end = timeit.default_timer()
print(f'Time execution: {(end-start):.10f}')
