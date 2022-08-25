class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def ligada(self):
        return self.__ligada

    def ligar_ou_desligar(self):
        if self.__ligada:
            self.__ligada = False
            return
        self.__ligada = True


class ContaCorrente:
    count = 999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.count + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.count = self.__numero


class Produto:
    count = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.count
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.count = self.id

    @property
    def valor(self):
        return self.__valor

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return self.valor * (1 - porcentagem / 100)


lamp1 = Lampada(cor='branca', voltagem=220)
cc1 = ContaCorrente(5000, 22500)
prod1 = Produto("Notebook", "Notebook Dell Inspiron", 5000.99)
#
# print(f'lamp1 está ligada: {lamp1.ligada}')
# lamp1.ligar_ou_desligar()
# print(f'lamp1 está ligada: {lamp1.ligada}')
# lamp1.ligar_ou_desligar()
# print(f'lamp1 está ligada: {lamp1.ligada}')

print(prod1._Produto__nome)  # Name mangling. Não recomendado
