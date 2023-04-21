class Produkt:
    """Pierwsza klasa"""
    rodzaj = "produkt"
    kategorji = {}

    def __init__(self, cena, nazwa, kategorja):
        self.cena = cena
        self.nazwa = nazwa
        self.kategorja = kategorja

        if kategorja in Produkt.produkty:
            Zwierz.zwierzeta[gatunek] += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1

    def podaj_gatunek(self):
        print("lis")

    def oblicz_odliglosc(self, czas):
        print(czas * self.max_predkosc)


    def _sprawdz_stan_zdrowia(self):
        if self.stan_drowia == 1:
            return 1
        else:
            return 0

    @staticmethod
    def wypisz_zwierzenta():
        print(Zwierz.zwierzeta)

    # Nadpisanie zmiennej specjalnej
    def __str__(self):
        return self.gatunek + " ma " + str(self.wiek) + " lat i osiaga predkosc " + str(self.max_predkosc) + " km/h."
