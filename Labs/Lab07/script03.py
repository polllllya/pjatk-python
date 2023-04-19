"""
Metody KLasy
"""

class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierze"
    zwierzeta = {}

    def __init__(self, gatunek, wiek, predkosc):
        self.gatunek = gatunek
        self.wiek = wiek
        self.max_predkosc = predkosc
        if gatunek in  Zwierz.zwierzeta:
            Zwierz.zwierzeta[gatunek] += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1

    def podaj_gatunek(self):
        print("lis")

    def oblicz_odliglosc(self,czas):
        print(czas  * self.max_predkosc)

    @staticmethod
    def wypisz_zwierzenta():
        print(Zwierz.zwierzeta)

Zwierz.wypisz_zwierzenta()

a = Zwierz("lis",5,10)
b = Zwierz("phyton",3,4)

a.oblicz_odliglosc(2)
b.oblicz_odliglosc(2)

# Definiowanie metod na poziomie klas
Zwierz.wypisz_zwierzenta()