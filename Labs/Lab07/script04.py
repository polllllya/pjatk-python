"""
Metody Specjalne klas
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


    # Nadpisanie zmiennej specjalnej
    def __str__(self):
        return self.gatunek + " ma " + str(self.wiek) + " lat i osiaga predkosc " + str(self.max_predkosc)+" km/h."
    
a = Zwierz("lis",5)
print(a)