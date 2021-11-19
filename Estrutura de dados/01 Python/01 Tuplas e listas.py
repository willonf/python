tupla = ('Homo sapiens', 'Canis familiares', 'Felis catus')
print(tupla[0])
print(f"Homo sapiens está na posição {tupla.index('Homo sapiens')}")

for elemento in tupla:
    print(elemento)

lista1 = ['Homo sapiens', 'Canis familiares', 'Felis catus']
lista2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']
lista3 = lista1 + lista2
print(lista3)
print(lista1[0])
print(lista3[0::2])
lista1.append('Gorila gorila')
print(lista1)
lista1.remove('Felis catus')
print(lista1)
# del(lista1)
print(lista1)
for item in lista2:
    print(item)
