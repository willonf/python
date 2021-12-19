"""
É possível adicionar estruturas condicionais às list comprehensions
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = [number for number in numbers if number % 2 == 0]
print(evens)
print(40 * "=+")

odds = [number for number in numbers if number % 2 != 0]
print(odds)
print(40 * "=+")

evens = [number for number in numbers if not number % 2]
print(evens)
print(40 * "=+")

odds = [number * 2 if number % 2 == 0 else number/2 for number in numbers]
print(odds)
print(40 * "=+")
