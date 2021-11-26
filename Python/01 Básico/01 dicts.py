dictionary1 = dict()
dictionary2 = {}
dictionary3 = dict(a=2, b=1, c=0)

dictionary1.update({'br': 'Brasil'})
print(dictionary1)

dictionary2.update({'pt': 'Portugal', 'us': 'United States'})

print(dictionary1.get('br'))
print(dictionary1['br'])
print(dictionary2.get('pt'))
print(dictionary2.get('us'))

print(dictionary2.get('br', 'Not found'))
# Verificando se existe uma chave no dicionário:
print('br' in dictionary1)

dictionary1.update({'uk': 'United K'})
dictionary1['uk'] = 'United Kingd'
dictionary1.update({'uk': 'United Kingdom'})
print(dictionary1['uk'])

# Em dicionários precisamos sempre passar uma key no método "pop"
dictionary2.pop('pt')
print(dictionary2)
del dictionary2['us']
print(dictionary2)

print(dictionary3)
print(dictionary3.keys())
print(dictionary3.values())

dict_novo = dictionary3.copy()
print(dict_novo)
dict_novo.update({'new_key': 1})
print(dict_novo)
new_dict_2 = dictionary3
new_dict_2.update({'key': 2})
print(new_dict_2)
print(dictionary3)

# Forma não usual de criar dicionários
usuario = {}.fromkeys(['Key 1', 'Key 2', 'Key 3'], 'valor')
print(usuario)
usuario2 = {}.fromkeys(['Key 1', 'Key 2', 'Key 3'], ['valor', 'valor', 'valor'])
print(usuario2)

meses = {'Jan': 30, 'Fev': 28, 'Mar': 31}

for mes in meses:
    # Todas as chaves serão impressas
    print(mes)

for mes in meses:
    # Todas os valores serão impressos
    print(meses[mes])


for k, v in enumerate(meses):
    # Todas os valores serão impressos
    print(f'{k}: {v}')
