"""
open() recebe o nome do arquivo e esta retorna um _io.TextIOWrapper,
objeto que usamos para leitura e escrita.
Por padrão, a função open() abre o arquivo em modo de leitura.
O arquivo deve exister, se não ocorre o erro FileNotFoundError

O método read() lê o arquivo inteiro. Pode receber como parâmetro a quantidade
de caracteres que se deseja ler.
Modos: r,w,x,a,b,t,U, + (leitura e escrita)
"""

try:
    file = open('text', mode='r', encoding='UTF-8')
    print(file.read())
    # print(file.read())

except FileNotFoundError as error:
    print(error.strerror)
