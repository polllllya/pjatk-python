import random

def wygeneruj_liste(ilosc_el, poczatek, koniec):
    liczby = [random.randint(poczatek, koniec) for _ in range(ilosc_el)]
    return liczby

# Sprawdzenie działania
# lista = wygeneruj_liste(20,1,100)
# print(lista)