import numpy as np


class VetorNaoOrdenado:
    def __init__(self, tamanho, tipo):
        self.tamanho = tamanho
        self.ultimaPosicao = -1
        self.elementos = np.empty(self.tamanho, dtype=tipo)

    def inserir(self, *argv):
        for arg in argv:
            if self.ultimaPosicao == self.tamanho - 1:
                print(f'Vetor cheio! Tamanho máximo: {self.tamanho}')
                return
            else:
                self.ultimaPosicao += 1
                self.elementos[self.ultimaPosicao] = arg
                print(f'Inseri {argv[self.ultimaPosicao]}')

    def imprimir(self):
        if self.ultimaPosicao == -1:
            print('Vetor vazio')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f'{self.elementos[i]}')

    def buscar(self, elemento):
        posicao = -1
        for i in range(self.ultimaPosicao + 1):
            if elemento == self.elementos[i]:
                posicao = i
        return posicao

    def excluir(self, elemento):
        posicao = self.buscar(elemento)
        if posicao == -1:
            return ('Não encontrado. -1')
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.elementos[i] = self.elementos[i+1]
            self.ultimaPosicao -= 1
            return ('Excluído')


vetor = VetorNaoOrdenado(5, float)

print(f"{5*'+='} INSERINDO ELEMENTOS NO VETOR {5*'+='}")
print('Inserindo o número 2.5 -7.6, -10, -11, 0 e 2')
vetor.inserir(2.5, -7.6, -10, -11, 0, 2)


print(f"{5*'+='} EXIBINDO ELEMENTOS DO VETOR {5*'+='}")
vetor.imprimir()

print(f"{5*'+='} BUSCANDO ELEMENTOS DO VETOR {5*'+='}")
print(f'Buscando o elemento -7.6 ... Posição: {vetor.buscar(-7.6)}')
print(f'Buscando o elemento -8 ... Posição: {vetor.buscar(-8)}')
print(f'Buscando o elemento 2.5 ... Posição: {vetor.buscar(2.5)}')
print(f'Buscando o elemento -10 ... Posição: {vetor.buscar(-10)}')

print(f"{5*'+='} EXCLUINDO ELEMENTOS DO VETOR {5*'+='}")
print(f'Excluindo o elemento -8 ... {vetor.excluir(-8)}')
print(f'Excluindo o elemento -10 ... {vetor.excluir(-10)}')
print(f'Excluindo o elemento 2.5 ... {vetor.excluir(2.5)}')
print(f"{5*'+='} NOVO VETOR {5*'+='}")
vetor.imprimir()

print(f"{5*'+='} VETOR ATUAL {5*'+='}")
print(vetor.elementos)
