# O polimorfismo ocorre quando há reimplementação de métodos da super classe na classe filha

# Essa reimplementação pode ser de sobrecarga(overloading) ou de sobrescrita (overriding).

# Python não tem sobrecarga de métodos

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):  # Overriding
        print(f'{self._Animal__nome} fala au au au')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):  # Overriding
        print(f'{self._Animal__nome} fala miau miau miau'),


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):  # Overriding
        print(f'{self._Animal__nome} falata sniiasniansid')

    def comer(self, comida):  # Não é um overloading. ACeita, mas não é comum usar isso
        print(f'Eu só gosto de comer {comida}!')


felix = Gato('Felix')
pluto = Cachorro('Pluto')
mickey = Rato('Mickey')

felix.comer()
felix.falar()

pluto.comer()
pluto.falar()

mickey.comer('cenoura')
mickey.falar()
