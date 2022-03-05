import datetime, timeit

# Timezones

# Com o now() podemos especificar o TZ, diferente do today()
now = datetime.datetime.now()
print(now)

today = datetime.datetime.today()
print(today)

# Mudanças à meia-noite. combine()
manutencao = datetime.datetime.combine((datetime.datetime.now()) + datetime.timedelta(days=1), datetime.time())
print(manutencao)

# Dia da semana. Começa em 0 (segunda-feira), 1 (terça-feira), ..., 6 (domingo)
print(manutencao.weekday())

# Formatando datas com strftime() (String format time)

hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')
hoje_formatado1 = hoje.strftime('%A/%B/%Y')
print(hoje_formatado)
print(hoje_formatado1)

nascimento = datetime.datetime.strptime('12/04/1995', '%d/%m/%Y')
print(nascimento)

# Trabalhando com hora
almoco = datetime.time(hour=12, minute=30, second=0)
print(almoco)

# Marcando tempo de execução
tempo1 = timeit.timeit(
    '"-".join(str(n) for n in range(0, 100))', number=1000
)
tempo2 = timeit.timeit(
    '"-".join([str(n) for n in range(0, 100)])', number=1000
)
print(tempo1)
print(tempo2)
