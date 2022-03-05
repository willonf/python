import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(year=1995, month=4, day=12)
periodo = data_hoje - aniversario
print(type(periodo))
print(repr(periodo))
print(periodo)

delta = datetime.timedelta(days=365)
periodo = periodo + delta
print(periodo)
print(delta)
