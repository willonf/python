def comer(comida, eh_saudavel):
    if eh_saudavel is None:
        return None
    return 'É saudável' if eh_saudavel else 'Não é saudável'


def dormir(num_horas):
    return 'Boa noite' if num_horas >= 7 else 'Durma mais'
