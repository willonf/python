my_set1 = set()
my_set2 = {1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 15, 15, 12, 12}
my_set3 = set((1, 1, 1, 1, 2, 2, 2, 3, 4, 9, 9, 9, 5, 5, 5, 5, 5))
my_set1.update(range(10))
my_set1.update(range(10))

print(my_set1)
print(my_set2)
print(my_set3)

my_set1.add(45)
print(my_set1)
print(my_set1.pop())
print(my_set1.pop())
my_set1.remove(5)
print(my_set1)

# Realizando união de conjuntos
print(my_set1)
print(my_set1.union(my_set2))
print(my_set1 | my_set2)

# Realizando interseção de conjuntos
print(my_set1.intersection(my_set2))
print(my_set1 & my_set2)

# Realizando diferença de conjuntos
print(my_set1.intersection(my_set2))
print(my_set1 & my_set2)
