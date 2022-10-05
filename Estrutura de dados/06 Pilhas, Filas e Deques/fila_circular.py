import numpy as np


class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia!')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print('Fila vazia!')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1
        return self.valores[self.inicio]


fila = FilaCircular(3)
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print(fila.valores)
