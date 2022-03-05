print(1, 2, 3, 4, 5, 6, sep='.')
print(1, 2, 3, 4, 5, 6, sep='a')
print(1, 2, 3, 4, 5, 6, sep=' ')
print(1, end=' ')
print(2, end=' ')
print(3, end='\n')

site = 'Python Academy'
titulo = 'f-string no Python'
dificuldade = 'Básico'

print(
    f"Site: {site}\n"
    f"Título: {titulo}\n"
    f"Dificuldade: {dificuldade}"
)
# Formatação: %[flags][width][.precision]type
# https://python-course.eu/python-tutorial/formatted-output.php
num1 = 900000
num2 = 700
div = num1 / num2
print(f'{div:,.4f}')
print(f'{div:_.4f}')
print(f'{div:.4f}')

nome = 'Willon'
print(f'{nome=}')
print("Willon".center(20, '#'))
print("Willon".rjust(20, '#'))
print("Willon".ljust(20, '#'))

nome: str = 'Willon'
print(nome)
