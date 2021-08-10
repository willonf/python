import re
frase1 = 'Olá, meu número de telefone é (92)99332-1276'
frase2 = 'A placa de carro que eu anotei durante o acidente foi FRT-1998, '
email = 'Entre em contato, meu email é contatowillon@gmail.com'
# Procurando um telefone na string
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase1))
# Procurando uma placa de carro na string
print(re.search('[A-Z]{3}-\d{4}', frase2))
# Procurando um e-mail na string
print(re.search('\w+@\w+\.\w+(.br)*', email))

frase3 = 'Meu número de telefone atual é (42)00000-0000. O número (56)1111-1111 é o antigo'
telefones = re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3)
print(telefones)
print(telefones[0])
print(telefones[1])
