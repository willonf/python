import re as regex
listaDeCEPs = '''Alagoas: 57000-000 a 57099-999;
                Paraiba: 58000-000 a 58099-999
                Ceará: 60000-000 a 60999-999,
                Amazonas: 69000-000 a 69099-999'''
listaDeFones = ''' Telefones úteis: (92)99332-1276
                (92)8257-3354 (85)98878-6578'''

print(regex.findall('\d{5}-\d{3}', listaDeCEPs))
print(regex.findall('\(\d{2}\)\d{4,5}-\d{4}', listaDeFones))
