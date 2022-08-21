import numpy as np


class VetorNaoOrdenado:

    def __init__(self, lenght):
        self.length = lenght
        self.lastPosition = -1
        # np.empty() cria um vetor vazio de tamanho fixo, com o tipo escolhido:
        self.values = np.empty(self.length, dtype=int)  # dtype = Data type

    # Big-O: O(n)
    def imprime(self):
        if self.lastPosition == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.lastPosition + 1):
                print(f'Posição {i}: {self.values[i]}')

    # Big-O: O(1) - O(2), ou seja, constante O(1)
    def inserir(self, value):
        if self.lastPosition == self.length - 1:
            print('Capacidade máxima atingida')
            return
        else:
            self.lastPosition += 1
            # Inserindo na última posição do vetor numpy:
            self.values[self.lastPosition] = value

    # Big-O: O(n)
    def pesquisar(self, value):
        for i in range(self.length):
            if value == self.values[i]:
                return i
        return -1

    # Big-O: O(n)
    def excluir(self, value):
        index = self.pesquisar(value)
        if index == -1:
            print('Not found. (-1)')
        else:
            for i in range(index, self.lastPosition):
                self.values[i] = self.values[i+1]
            self.lastPosition -= 1


vetor = VetorNaoOrdenado(5)

print(15*'+=')
vetor.imprime()
print(15*'+=')

print('Inserindo os elementos e imprimindo:')
vetor.inserir(2)
vetor.inserir(-3)
vetor.inserir(4)
vetor.inserir(-5)
vetor.inserir(1)
print(15*'+=')

vetor.inserir(1)  # Saída: Capacidade máxima atingida
print(15*'+=')

print(f'Posição do elemento (1): {vetor.pesquisar(1)}')
print(f'Posição do elemento (-11): {vetor.pesquisar(-11)}')
print(f'Posição do elemento (4): {vetor.pesquisar(4)}')
print(f'Posição do elemento (-3): {vetor.pesquisar(-3)}')
print(15*'+=')

vetor.excluir(2)  # Excluído
vetor.excluir(4)  # Excluído
vetor.excluir(-11)  # Not found. -1
vetor.excluir(1)  # Excluído
vetor.imprime()
print(15*'+=')

print(vetor.values)
print(vetor.lastPosition)
print(vetor.length)
