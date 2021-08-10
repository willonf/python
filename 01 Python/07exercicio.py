lista = []
try:
    lista.append(float(input('Digite o primeiro valor do tipo float:\n')))
    lista.append(float(input('Digite o primeiro valor do tipo float:\n')))
    divisao = lista[0]/lista[1]
    print(f'Lista: {lista}')
except Exception as error:
    print('Não é possível dividir por 0.')
    print(error.__class__)
except ValueError:
    print('Valor digitado não corresponde ao tipo pedido')
except IndexError:
    print('Elemento fora do alcance da lista')
    print()
except KeyboardInterrupt:
    print('Usuário interrompeu a execução do programa.')
else:
    print(f'A divisão é: {divisao:.2f}')
finally:
    print('Obrigado por usar o nosso software. Volte sempre!')
