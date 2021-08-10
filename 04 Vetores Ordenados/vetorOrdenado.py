import numpy as np


class VetorOrdenado:
    def __init__(self, length, type):
        self.length = length
        self.lastPosition = -1
        self.values = np.empty(self.length, type)

    def insert(self, element):
        if self.lastPosition == self.length - 1:
            print('Vetor cheio!')
            return
        # Encontrando a posição onde será inserindo o elemento:
        position = 0
        for i in range(self.lastPosition + 1):
            position = i
            if self.values[i] > element:
                break
        # Todo o vetor foi percorrido e não obteve-se:
            if i == self.lastPosition:
                position = i + 1
        # Remanejando os elementos
        currentPosition = self.lastPosition
        while currentPosition >= position:
            self.values[currentPosition + 1] = self.values[currentPosition]
            currentPosition -= 1
        self.values[position] = element
        self.lastPosition += 1

    def search(self, element):
        for i in range(self.lastPosition + 1):
            if self.values[i] > element:
                return -1
            elif self.values[i] == element:
                return i
            elif i == self.lastPosition:
                return -1

    def binarySearch(self, element):
        lowBound = 0
        highBound = self.length - 1
        while True:
            midBound = (lowBound + highBound) // 2
            # Achou na primeira tentativva
            if self.values[midBound] == element:
                return midBound
            elif lowBound > highBound:
                return -1
            elif self.values[midBound] < element:
                lowBound = midBound + 1
            else:
                highBound = midBound - 1

    def remove(self, element):
        index = self.search(element)
        if index == -1:
            return -1
        else:
            for i in range(index, self.lastPosition):
                self.values[i] = self.values[i+1]
            self.lastPosition -= 1

    def show(self):
        if self.lastPosition == -1:
            print('Vetor vazio. -1')
        else:
            for i in range(self.lastPosition + 1):
                print(f'[{i}] = {self.values[i]}')


array = VetorOrdenado(5, int)

print(f"{5*'+='} INSERINDO ELEMENTOS NO VETOR {5*'+='}")
print('Inserindo o elemento 1 ...')
array.insert(1)
print('Inserindo o elemento 10 ...')
array.insert(10)
print('Inserindo o elemento 12 ...')
array.insert(12)
print('Inserindo o elemento 5 ...')
array.insert(5)
print('Inserindo o elemento -2 ...')
array.insert(-2)
print('Inserindo o elemento -4 ...')
array.insert(-4)
print('Inserindo o elemento -59 ...')
array.insert(-59)

print(f"{5*'+='} EXIBINDO ELEMENTOS DO VETOR {5*'+='}")
array.show()

print(f"{5*'+='} BUSCANDO ELEMENTOS DO VETOR (BUSCA LINEAR) {5*'+='}")
print(f'Buscando o elemento 12 ... Posição [{array.search(12)}]')
print(f'Buscando o elemento -8 ... Posição [{array.search(-8)}]')
print(f'Buscando o elemento 1 ... Posição [{array.search(1)}]')
print(f'Buscando o elemento 10 ... Posição [{array.search(10)}]')
print(f'Buscando o elemento 15 ... Posição [{array.search(15)}]')

print(f"{5*'+='} BUSCANDO ELEMENTOS DO VETOR (BUSCA BINÁRIA) {5*'+='}")
print(f'Buscando o elemento 12 ... Posição [{array.binarySearch(12)}]')
print(f'Buscando o elemento -8 ... Posição [{array.binarySearch(-8)}]')
print(f'Buscando o elemento 1 ... Posição [{array.binarySearch(1)}]')
print(f'Buscando o elemento 10 ... Posição [{array.binarySearch(10)}]')
print(f'Buscando o elemento 15 ... Posição [{array.binarySearch(15)}]')

print(f"{5*'+='} EXCLUINDO ELEMENTOS DO VETOR {5*'+='}")
print('Removendo o elemento 12 ...')
array.remove(12)
array.show()
print('Removendo o elemento 5 ...')
array.remove(5)
array.show()
print('Removendo o elemento -2 ...')
array.remove(-2)
array.show()

print(f"{5*'+='} VETOR ATUAL {5*'+='}")
array.show()
