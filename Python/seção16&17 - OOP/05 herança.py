class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # A classe Cliente herda a classe Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Sobrescrita (Override): Reescrita de métodos em classes herdadas, mas utilizando a mesma assinatura
    # Assinatura de uma classe: nome + parâmetros
    def nome_completo(self):
        return f'Funcionário: {self._Pessoa__nome} - {self.__matricula}'


cliente1 = Cliente(nome='Angelina', sobrenome='Jolie', cpf='123.456.789-10', renda=5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-10', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
