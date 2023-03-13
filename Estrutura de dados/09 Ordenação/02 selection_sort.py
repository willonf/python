# O Selection Sort percorre todos os elementos e seleciona o menor.
# O menor elemento é trocado com o elemento da extremidade esquerda do vetor (posições iniciais)
# Os elementos ordenados acumulam-se na esquerda
# Big-O: O(n²)


def selection_sort(array):
    length = len(array)
    for i in range(length):
        smaller_index = i
        # Começa sempre na próxima posição. A posição atual não precisa ser comparada com ela mesma
        for j in range(i + 1, length):
            if array[j] < array[smaller_index]:
                smaller_index = j
        temp = array[i]
        array[i] = array[smaller_index]
        array[smaller_index] = temp


array_numbers = [38, 5, 3, 2, 47, 15, 46, 44, 36, 26, 27]
print(array_numbers)
selection_sort(array_numbers)
print(array_numbers)
