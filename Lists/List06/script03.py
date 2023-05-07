from Lists.List07.funkcje import oblicz_wiek

class Osoba:

    def __init__(self, imie, nazwisko, plec, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.data_urodzenia = data_urodzenia
        self.wiek = oblicz_wiek(data_urodzenia)
    
    def wyswietl_info(self):
        return {'Imię': self.imie, 'Nazwisko': self.nazwisko, 'Płeć': self.plec, 'Data urodzenia': self.data_urodzenia,
                'Wiek': self.wiek}
    
    @staticmethod
    def wyswietl_osoby(osoby):
        return [osoba.wyswietl_info() for osoba in osoby]

class Gracz(Osoba):
    def __init__(self, imie, nazwisko, plec, data_urodzenia, nick, typ, email):
        super().__init__(imie, nazwisko, plec, data_urodzenia)
        self.nick = nick
        self.typ = typ
        self.email = email
    
    def wyswietl_info(self):
        info = super().wyswietl_info()
        info.update({'Nick': self.nick, 'Typ': self.typ, 'Email': self.email})
        return info
    
    @staticmethod
    def wyswietl_graczy(gracze):
        return {f'Gracz {i+1}': gracz.wyswietl_info() for i, gracz in enumerate(gracze)}


osoba1 = Osoba('Jan', 'Kowalski', 'm', '01.01.1990')
osoba2 = Osoba('Anna', 'Nowak', 'k', '02.02.1995')
gracz1 = Gracz('Piotr', 'Wójcik', 'm', '03.03.2000', 'piotr123', 'Human', 'piotr123@example.com')
gracz2 = Gracz('Karolina', 'Kaczor', 'k', '04.04.1998', 'karo456', 'NPC', 'karolina456@example.com')

osoby = [osoba1, osoba2]
gracze = [gracz1, gracz2]

print(Osoba.wyswietl_osoby(osoby))

print(Gracz.wyswietl_graczy(gracze))