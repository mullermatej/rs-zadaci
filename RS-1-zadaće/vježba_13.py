def prvi_i_zadnji(lista): return (lista[0], lista[-1])


def maks_i_min(lista):
    maks = min = lista[0]
    for broj in lista:
        if (broj > maks):
            maks = broj
        elif (broj < min):
            min = broj
    return (maks, min)


def presjek(skup_1, skup_2):
    novi_skup = set()
    for broj1 in skup_1:
        for broj2 in skup_2:
            if (broj1 == broj2):
                novi_skup.add(broj1)
    return novi_skup


lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

print(prvi_i_zadnji(lista))  # (5, 80)
print(maks_i_min(lista))  # (250, 5)
print(presjek(skup_1, skup_2))  # {4, 5}
