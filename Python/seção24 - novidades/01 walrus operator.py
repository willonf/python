nome = 'Willon'  # Atribuição
print(nome)  # Retorno

print(nome2 := 'Nolliw')  # Atribuição e retorno
print(nome2)

cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)

print(cesta)
