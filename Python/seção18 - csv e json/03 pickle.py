"""
Pickle
Processo de serialização/desserialização:
Objeto python -> Binarização
Binarização -> Objeto python

Obs.: O Pickle não é seguro contra dados maliciosos. Não é recomendado trabalhar
    com arquivos pickle oriundos de fontes que não sejam seguras.

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} está comendo...')




class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')

# Escrita de arquivos pickle
felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo:  # A extensão .pickle não é obrigatória.
    pickle.dump((felix, pluto), arquivo)

# Leitura de arquivos pickle

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato se chama {gato.nome}')
    gato.mia()
    print(f'O cachorro se chama {cachorro.nome}')
    cachorro.late()
