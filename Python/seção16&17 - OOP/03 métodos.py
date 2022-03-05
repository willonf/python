"""
Uma classe também pode ter métodos (de instância e de classe).

Os métodos dunder (como o __init__) são os métodos mágicos das classe.
    __init__: método construtor
"""


class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


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


class Usuario:
    count = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.count + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        print(f'Usuário criado: {self.__gera_usuario()}')
        Usuario.count = self.__id

    @classmethod  # Decorator para método de classe (método estático). Não tem acesso aos atributos de instância
    def conta_usuarios(cls):
        print(f'Temos {cls.count} usuários no sistema.')

    # def teste(self):  # Vai indicar que pode ser estático
    #     print('Teste!')

    @classmethod  # Método de classe (estático para outras linguagens), pois não usa nenhum atributo de instância
    def metodo_classe(cls):
        print('Método de classe!')

    @staticmethod  # Método estático no Python. Não possui acesso aos atributos da classe nem das instâncias
    def metodo_estatico():
        print('Método estático!')

    def __correr__(self, dist):  # Nomenclatura errada de método
        print(f'{self.__nome} está correndo {dist} km todo dia')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # Métodos privados - Iniciar com duplo underscore
    def __gera_usuario(self):
        return self.__email.split('@')[0]


user1 = Usuario('Willon', 'Ferreira', 'willon@gmail.com', '123456')
user2 = Usuario('Nolliw', 'Silva', 'nolliw@gmail.com', '654321')
user1.__correr__(12)
print(user1.nome_completo())

prod1 = Produto('PS5', 'Videogame PS5', 5000.00)
print(prod1.valor)
print(prod1.desconto(20))  # outra forma de escrever:
print(Produto.desconto(prod1, 20))  # O parâmetro self, recebe o objeto prod1 como argumento
print(30 * '+=')
user1.conta_usuarios()  # O resultado será o mesmo para as duas instâncias da classe Usuário
user2.conta_usuarios()  # Apesar de funcionar, é a forma incorreta de invocar esse método
Usuario.conta_usuarios()  # forma correta de chamada do método, pois o mesmo é um método da classe
user1.metodo_classe()
user1.metodo_estatico()

# print(user1.__gera_usuario())  # Vai gerar AttributeError
