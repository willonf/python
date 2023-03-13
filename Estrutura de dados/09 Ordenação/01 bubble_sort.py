# O Buble Sort funciona através de comparações.
# Se o elemento da esquerda for maior, os elementos devem ser trocados. Desloca-se uma posição à direita
# À medida que os algoritmos avançam, os itens maiores surgem como uma "bolha" na extremidade superior do vetor.
# Complexidade: O(n²)


def bubble_sort(array):
    length = len(array)

    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return array


print(bubble_sort([15, 34, 34, 8, 3]))
print(bubble_sort([34, 15, 8, 3]))
print(bubble_sort([3, 8, 15, 34]))
