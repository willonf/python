import numpy as np

# Uma pilha só concede acesso ao seu topo


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.valores = np.chararray(self.__capacidade, unicode=True)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        return False

    def pilha_vazia(self):
        if self.__topo == - 1:
            return True
        return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.valores[self.__topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print('A pilha está vazia')
            return -1
        else:
            valor = self.valores[self.__topo]
            self.__topo -= 1
            return valor

    def topo(self):
        if self.__topo != -1:
            return self.valores[self.__topo]
        return -1


expr = input('Digite uma expressão: ')
pilha = Pilha(len(expr))


for e in expr:
    if e in ('{', '[', '('):
        pilha.empilhar(e)
    elif e in ('}', ']', ')'):
        if not pilha.pilha_vazia():
            e2 = pilha.desempilhar()
            if (e == '}' and e2 != '{') or (e == ']' and e2 != '[') or (e == ')' and e2 != '('):
                print('Expressão inválida.')
                break
        else:
            print('Expressão inválida.')
            break
