"""
Lab07 - Klasy
"""

# Wszystko jest publicznie.

class Zwierz:
    """Pierwsza klasa"""

    def podaj_gatunek(self):
        print("lis")


a = Zwierz()
print(a)

b = Zwierz()
print(b)

# Sprawdzenie czy mamy do czynienia z tym samym obiektem
print(a == b)

# Wywołanie metody
a.podaj_gatunek()
b.podaj_gatunek()


