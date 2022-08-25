import json
import jsonpickle

# O dumps serializa um objeto python em json
ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220v', 2340)}])

print(type(ret))
print(ret)


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

    def mia(self):
        print(f'{self.nome} está miando...')


felix = Gato('Feliz', 'Vira-lata')

print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)

ret = jsonpickle.encode(felix)
print(ret)


# Escrevendo arquivo json
# with open('felix.json', 'w') as arquivo:
#     ret = jsonpickle.encode(felix)
#     arquivo.write(ret)


# Lendo arquivo json
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret.nome)
    print(ret.raca)
