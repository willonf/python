"""
- Literal type
- Union
- Typed dictionaries
- Protocols
"""


def dobro(num: int) -> int:
    return 2 * num


print(dobro(2))
print(dobro('Will'))  # Com o pacote mypy é possível evitar isso

# Literal type
from typing import Literal


# A função pegar_status retornará uma string ('conectado' ou 'desconectado'
def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


def calcula(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(num1 + num2)
    elif operacao == '-':
        print(num1 - num2)


calcula('-', 2, 3)
calcula('*', 2, 3)

# Union
# O union pode unir tipos de retorno
from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    result = num1 + num2
    if result > 50:
        return f'O valor {result} é muito grande'
    else:
        return result


print(soma(2, 5))
print(soma(50, 5))

# Final

from typing import Final

NOME: Final = 'Geek'

print(NOME)
NOME = 'WILL'

from typing import final


@final
class Pessoa:
    pass


class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estou estudando e estagiando...')


# Typed dicts
from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.9', atualizacao=2021)
geek2 = CursoPython(outro1='3.9', outro=True)
print(geek)
print(geek2)

# Protocols

from typing import Protocol


class Curso(Protocol):
    titulo: str


class Venda1:
    pass


class Venda2:
    titulo = 'Ethical hacking'


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


v1 = Venda1()
v2 = Venda2()

# estudar(v1)
estudar(v2)

# A classe Venda2 segue o protocolo da classe Curso (atributos iguais),
# logo é possível usar a classe Venda2 como parâmetro na função estudar
# que aceita apenas parâmetros do tipo Curso
