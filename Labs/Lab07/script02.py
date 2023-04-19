"""
Inicjalizowanie klas i atrybuty klas
"""


class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierze"

    def __init__(self, gatunek, wiek):
        self.gatunek = gatunek
        self.wiek = wiek

    def podaj_gatunek(self):
        print("lis")


a = Zwierz("lis", 5)
b = Zwierz("python", 2)

print(a.gatunek, a.wiek)
print(b.gatunek, b.wiek)

# Definiowanie atrybutów poza klasa, ale tego unikać
b.długość = 10
print(b.długość)

# Wyświetlanie atrybutów wspólnych dla objektów klas
print(a.rodzaj,b.rodzaj)
print(Zwierz.rodzaj) # dla atrybutu statycznego

# Zmiana wartsci atrybutów
b.długość = 11
print(b.długość)
a.wiek = 6
print(a.wiek)

# Atrybuty specjalne
print(a.__dict__)
print(b.__dict__)

# Opis klasy
print(Zwierz.__doc__)
print(a.__doc__)