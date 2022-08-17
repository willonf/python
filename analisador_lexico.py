import re


class AnalisadorLexico:

    def __init__(self):
        self.TOKENS = {'+': 'OP_SOMA', '-': 'OP_SUB', '*': 'OP_PROD', '/': 'OP_DIV', '%': 'OP_MOD',
                         '=': 'OP_ATRIB', '(': 'ABRE_PARENT', ')': 'FECHA_PARENT',
                         'token_int': 'LIT_INT', 'token_float': 'LIT_FLOAT', 'def': 'FUNCTION_DEF',
                         'ident': 'IDENTIFICADOR'
                         }
        self.__IDENTIFICADOR = '[A-Za-z_][A-Za-z_0-9]*'
        self.__virgula = '\s*,\s*'
        self.__atribuicao = '\s*=\s*'
        self.__lista_params = '\((' + self.__IDENTIFICADOR + '?' + '(?:' + self.__virgula + self.__IDENTIFICADOR + ')*' + ')?\)'
        self.__declaracao_funcao = 'def\s+(' + self.__IDENTIFICADOR + ')\s*' + self.__lista_params + ':'
        self.__tipo_float_int = 'int|float'
        self.__chamada_funcao = '(' + self.__IDENTIFICADOR + self.__atribuicao + ')?\s*' + self.__IDENTIFICADOR + '\s*(\s*' + self.__lista_params + '\s*)\s*'
        self.__operadores = '[\+\-\*/%]'
        self.__literais_int_float = '[+-]?[0-9]+([.][0-9]*)?'
        self.__variavel = self.__IDENTIFICADOR + '(\s)*' + '(\s*)=(\s*)' + self.__literais_int_float
        # self.__expressao_aritmetica = '(' + self.__literais_int_float + ')+\s*' + self.__operadores + '\s*(' + self.__literais_int_float + ')+'
        self.__expressao_aritmetica = '([+-]?\d+([.]\d*)?\s*[\+\-\*/%]?\s*)'
        self.__regex_identificador = re.compile(self.__IDENTIFICADOR)
        self.__regex_funcao = re.compile(self.__declaracao_funcao)  # Corrigir
        self.__regex_type_int_float = re.compile(self.__tipo_float_int)
        self.__regex_chamada_funcao = re.compile(self.__chamada_funcao)
        self.__regex_literais_int_float = re.compile(self.__literais_int_float)
        self.__regex_variavel = re.compile(self.__variavel)
        self.__regex_expressao_aritmetica = re.compile(self.__expressao_aritmetica, flags=re.GLOBAL)

    @staticmethod
    def __is_numeric(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def __test_function(self, s):
        match = self.__regex_funcao.fullmatch(s)
        if match:
            return True
        return False

    def __test_tipo(self, s):
        match = self.__regex_type_int_float.fullmatch(s)
        if match:
            return True
        return False

    def __test_chamada_funcao(self, s):
        match = self.__regex_chamada_funcao.fullmatch(s)
        if match:
            return True
        return False

    def __test_literais_int_float(self, s):
        match = self.__regex_literais_int_float.fullmatch(s)
        if match:
            return True
        return False

    def __test_regex_variavel(self, s):
        match = self.__regex_variavel.fullmatch(s)
        if match:
            return True
        return False

    def __test_regex_expressao_aritmetica(self, s):
        match = self.__regex_expressao_aritmetica.fullmatch(s)
        if match:
            return True
        return False

    def __get_tokens(self, expr):
        result = ''
        token = None
        print(f'EXPRESSION: {expr}')
        for e in expr:
            if e.isdigit():
                token = self.TOKENS.get('token_int')
            elif self.__is_numeric(e):
                token = self.TOKENS.get('token_float')
            elif e.isalpha():
                token = self.TOKENS.get('ident')
            else:
                token = self.TOKENS.get(e, None)
            if token is not None:
                result = result + f'{e} -> {token}\n'

        print(result)
        # return result

    def analisar(self, expr):
        condition = self.__test_function(expr) or \
                    self.__test_tipo(expr) or \
                    self.__test_chamada_funcao(expr) or \
                    self.__test_literais_int_float(expr) or \
                    self.__test_regex_variavel(expr) or \
                    self.__test_regex_expressao_aritmetica(expr)

        if condition:
            self.__get_tokens(re.split('[\s*]+', expr))
        return f'Not valid expression'




try:
    analisador = AnalisadorLexico()
    with open('cases.txt', 'r') as file:
        expr = file.readline()
        analisador.analisar(expr)
except FileExistsError:
    print('Arquivo de cases inexistente')

except FileNotFoundError:
    print('Arquivo não encontrado')
