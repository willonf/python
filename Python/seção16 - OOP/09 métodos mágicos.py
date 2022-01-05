class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # Faz a representação do objeto
        return self.titulo

    def __str__(self):  # Faz a representação do objeto. Tem precedência sobre o __repr__
        return f'{self.titulo} - {self.autor} - {self.paginas}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        return f'{self.titulo} - ' * other if type(other) == int else 'Impossível multiplicar'


class Filme:
    def __init__(self, titulo):
        self.titulo = titulo


livro = Livro('Harry Potter', 'J.K. Rowlling', 1200)
filme = Filme('O Senhor dos Anéis')

print(livro)
print(str(livro))
print(repr(livro))
print(livro.__len__())
print(len(livro))
# livro.__del__()
# Após o encerramento do programa, o objeto é deletado da memória, chamando também o método __del__
print(livro + ' Livro 2')
print(livro*3)
print(livro*3.5)
print(filme)
