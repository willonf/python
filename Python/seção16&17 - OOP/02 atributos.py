"""
___init___(): Método construtor para declaração dos atributos.
    Também é possível usar o decorator @property, proporcionando melhor semantica


Visibilidade de atributos: em Python, por convenção, ficou estabelecido que todo atributo deve ser público.
    Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, utiliza-se dunder score (__)
        no início do nome. Isso se chama Name Mangling
"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite


class Teste:
    def __init__(teste):
        teste.__nome = 'Self pode receber outro nome'
        teste.__convencao = 'Por convenção usamos self (semelhante ao this do Java)'


class Acesso:
    # Atributos estáticos (atributos de classe)
    dominio = 'google.com'
    count = 0

    # Atributos de instância
    def __init__(self, nome, email, senha):
        self.id = Acesso.count + 1
        self.nome = nome  # Atributo público
        self.__dominio = Acesso.dominio  # Atributo privado
        self.__email = email  # Atributo privado
        self.__senha = senha  # Atributo privado
        Acesso.count = self.id  # ou seja, Acesso.count + 1


my_lamp = Lampada(220, 'Azul')
my_account = ContaCorrente(12041995, 10000, 6000)
print(my_lamp.cor)
print(my_account.numero)
# print(my_account.__saldo)  # Saldo é 'privado'

ac1 = Acesso('Willon', 'contatowillon@gmail.com', '123456')
ac2 = Acesso('Willon', 'contatowillon@gmail.com', '123456')
print(ac1.nome)
print(ac1.id)
print(ac2.id)

# Atributos dinâmicos - atributos criados em tempo de execução para uma instância

ac3 = Acesso('Nolliw', 'contatonolliw@gmail.com', '123456')
ac3.idade = 26
print(ac3.idade)
# print(ac1.idade)  # Vai gerar AttributeError

# Deletando atributos
del ac3.idade
del ac1.nome

print(ac3.__dict__)  # Não possui mais o atributo idade e count
print(ac1.__dict__)  # Não possui mais o atributo nome
print(ac1.__dict__)  # Não possui mais o atributo nome
