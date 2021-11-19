import numpy as np


class VetorOrdenado:

    def __init__(self, tamanho, *argv):
        self.tamanho = tamanho
        self.ultimaPosicao = -1
        self.valores = np.empty(self.tamanho, int)

    def __iter__(self):
        return self.valores.__iter__()

    def inserir(self):
        pass

    def imprimir(self):
        if (self.ultimaPosicao == -1):
            print('Vetor vazio!')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f'{[i]}: {self.valores[i]}')

    def pesquisa(self):
        pass

    def pesquisaBinaria(self):
        pass


vetor = VetorOrdenado(5, 87, 84)
vetor.imprimir()
