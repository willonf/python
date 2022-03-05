import datetime

print(dir(datetime))
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.datetime.now())
print(repr(datetime.datetime.now()))
print(datetime.datetime(2022, 3, 6, 20, 54, 12, 12))
print(30 * '=-')
# Ajustes com replace()
inicio = datetime.datetime.now()
print(inicio)
inicio = inicio.replace(hour=8, minute=0, second=0)
print(inicio)
print(30 * '=-')
# Acesso individual aos elementos

evento = datetime.datetime.now()
print(evento.year)
print(evento.hour)
print(evento.minute)

print(30 * '=-')

nascimento = input("Digite a data do seu nascimento (DD-MM-AAAA): ")
nascimento = nascimento.split('/')
nascimento.reverse()
nascimento = list(map(int, nascimento))
data_nascimento = datetime.datetime(*nascimento)
print(data_nascimento)
print(type(data_nascimento))
