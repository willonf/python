import numpy as np

# Uma pilha só concede acesso ao seu topo
class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)
    

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        return False
    

    def __pilha_vazia(self):
        if self.__topo ==  - 1:
            return True
        return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia')
        else:
            self.__topo -= 1
    

    def topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        return -1


pilha = Pilha(5)


print(pilha.topo())
pilha.empilhar(1)
print(pilha.topo())
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(6)  # Pilha cheia
print(pilha.topo())
pilha.desempilhar()
print(pilha.topo())