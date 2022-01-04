import unittest

from functions import comer, dormir

"""
Todos os test cases devem ter seu nome iniciado por 'test_'
Existem diversos tipos de asserts: assertIs, assertFalse, assertTrue, assertIsNone

hooks: São os testes em si, a execução deles

setup() -> método executado antes de cada método de teste.
    Útil para criamos instâncias de objetos e carregarmos outros dados

tearDown() -> é executado ao final de cada método de teste.
    Útil para excluir dados ou fechar conexões com banco de dados.
    
setUpClass
tearDownClass

"""


# geralmente, coloca-se o nome da classe com o mesmo
# nome do módulo que está sendo testado
class Secao20Test(unittest.TestCase):

    def setUp(self) -> None:
        print('O teste vai começar!')

    def test_comer_quiabo(self):
        """Teste com comida saudável"""
        self.assertEqual(comer('quiabo', True), 'É saudável')

    def test_comer_pizza(self):
        """Teste com comida não saudável"""
        self.assertEqual(comer('pizza', False), 'Não é saudável')

    def test_comer_pizza_none(self):
        self.assertEqual(comer('pizza', None), 'Não é saudável')

    def test_dormir_ok(self):
        self.assertEqual(dormir(7), 'Boa noite')

    def test_dormir_nao_ok(self):
        self.assertEqual(dormir(6), 'Durma mais')

    def tearDown(self) -> None:
        print('Teste encerrado!')


if __name__ == '__main__':
    unittest.main()
