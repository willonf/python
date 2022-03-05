"""
Herança múltipla - possibilidade de uma classe receber herança de diversas classes.
Pode ocorrer de duas maneiras:
    - Por multiderivação direta
    - Por multiderivação indireta

"""


# Multiderivação direta - A classe herda diretamente das superclasses

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiderivadaDireta(Base1, Base2, Base3):
    pass


# Multiderivação indireta - A classe não herda diretamente das superclasses

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiderivadaIndireta(Base3):
    pass


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Meu nome é {self.__nome}'

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'

    def cumprimentar(self):
        return f'Eeu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


happy_feet = Pinguim("Mano")
print(happy_feet.cumprimentar())  # Vai executar o método da classe herdada que vem na frente
# O comportamento acima acontece por causa do MRO (Method Resolution Order)
print(happy_feet.andar())
print(happy_feet.nadar())

# Como saber se um objeto é uma instância de outra classe?

print(isinstance(happy_feet, Pinguim))
print(isinstance(happy_feet, Aquatico))
print(isinstance(happy_feet, Terrestre))
print(isinstance(happy_feet, Animal))
print(isinstance(happy_feet, Base1))
print(isinstance(happy_feet, object))  # Toda classe herda de object

# O MRO pode ser conferido de 3 formas:
#   -Via __mro__
#   -Via método mro()
#   -Via help

print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))
