coleta = {'Aedes Aegypt': 32,
          'Aedes Albopictus': 22,
          'Anopheles Darlingi': 14}
print(coleta['Aedes Aegypt'])
coleta['Rhodnius Montenegrensis'] = 11
print(coleta)
del(coleta)['Aedes Albopictus']
print(coleta)
print(coleta.items())
print(coleta.keys())
print(coleta.values())
coleta2 = {'Anopheles Gambiae': 13,
           'Anopheles Deaneorum': 14}
print(coleta2)
coleta.update(coleta2)
print(coleta)
for especie, num_especimes in coleta.items():
    print(f'Espécie: {especie}, qtde. coletada: {num_especimes}')


biomoleculas = ('proteínas', 'ácidos nucleicos', 'carboidratos',
                'lipídeos', 'ácidos nucleicos', 'carboidratos')
print(biomoleculas)
print(set(biomoleculas))
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
print(conjunto1.intersection(conjunto2))
print(conjunto1.difference(conjunto2))
print(conjunto2.difference(conjunto1))
