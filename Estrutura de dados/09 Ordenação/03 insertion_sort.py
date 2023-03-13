# O Insertion Sort é cerca de 2x mais rápido que o Bubble Sort.
# Também é um pouco mais rápido que o Selection Sort
# Muito eficiente em dados quase ordenados.
# Para ordem inversa, é mais lento que o Bubble Sort, pois realiza todas as comparações e deslocamentos
# Funcina com um marcador em algum lugar no meio do vetor.
# Os elementos à esquerda estão parcialmente ordenados (mas não em suas posições finais).
# Os elementos da direita não estão ordenados.
# Big-O: O(n²)

def insertion_sort(array):
    length = len(array)

    for i in range(1, length):
        mark = array[i]
        j = i - 1

        while j >= 0 and mark < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = mark


array_numbers = [38, 5, 3, 2, 47, 15, 46, 44, 36, 26, 27]
print(array_numbers)
insertion_sort(array_numbers)
print(array_numbers)
