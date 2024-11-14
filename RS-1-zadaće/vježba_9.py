lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def ukloni_duplikate(lista):
    return list(set(lista))


print(ukloni_duplikate(lista))
