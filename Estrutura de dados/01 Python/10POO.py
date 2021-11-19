class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)/2

    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'não é um triângulo'
        elif self.lado1==self.lado2==self.lado3:
            return 'é um triângulo equilatéro'
        else:
            return 'é outro tipo de triângulo'

triang1 = Triangulo(1, 1, 1, 3, 4)
print(f'Lado 1: {triang1.lado1}')
print(f'Lado 2: {triang1.lado2}')
print(f'Lado 3: {triang1.lado3}')
print(f'Base: {triang1.base}')
print(f'Altura: {triang1.altura}')
print(f'Área: {triang1.area()}')
print(f'Tipo: {triang1.tipo()}')
