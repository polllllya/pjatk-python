class TokenGenerator:
    def __init__(self, klucz):
        self.klucz = klucz

    def szyfruj(self, tekst):
        zaszyfrowany_tekst = ""
        for znak in tekst:
            if znak.isalpha():
                if znak.isupper():
                    kod_znak = (ord(znak) - ord('A') + self.klucz) % 26 + ord('A')
                else:
                    kod_znak = (ord(znak) - ord('a') + self.klucz) % 26 + ord('a')
                zaszyfrowany_tekst += chr(kod_znak)
            else:
                zaszyfrowany_tekst += znak
        return zaszyfrowany_tekst

    def deszyfruj(self, tekst):
        odszyfrowany_tekst = ""
        for znak in tekst:
            if znak.isalpha():
                if znak.isupper():
                    kod_znak = (ord(znak) - ord('A') - self.klucz) % 26 + ord('A')
                else:
                    kod_znak = (ord(znak) - ord('a') - self.klucz) % 26 + ord('a')
                odszyfrowany_tekst += chr(kod_znak)
            else:
                odszyfrowany_tekst += znak
        return odszyfrowany_tekst


class Token:
    def __init__(self, imie, nazwisko, email, data_waznosci, klucz):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.data_waznosci = data_waznosci
        self.klucz = klucz

    def generuj_token(self):
        generator = TokenGenerator(self.klucz)
        dane_uzytkownika = f"{self.imie}.{self.nazwisko}.{self.email}.{self.data_waznosci}"
        zaszyfrowane_dane = generator.szyfruj(dane_uzytkownika)
        return zaszyfrowane_dane

    def odczytaj_dane(self, token):
        generator = TokenGenerator(self.klucz)
        odszyfrowane_dane = generator.deszyfruj(token)
        dane_uzytkownika = odszyfrowane_dane.split('.')
        if len(dane_uzytkownika) == 4:
            data_waznosci = ""
            for znak in dane_uzytkownika[3]:
                if znak.isalpha():
                    kod_znak = (ord(znak.upper()) - ord('A') - self.klucz) % 26 + ord('A')
                    litera = chr(kod_znak)
                    data_waznosci += litera
                else:
                    data_waznosci += znak
            dane_uzytkownika[3] = data_waznosci
            return dane_uzytkownika
        else:
            return None


imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
email = input("Podaj adres e-mail: ")
data_waznosci = input("Podaj datę ważności tokena (RRRR-MM-DD): ")
klucz = int(input("Podaj klucz (liczba całkowita): "))

token = Token(imie, nazwisko, email, data_waznosci, klucz)
wygenerowany_token = token.generuj_token()
print("Wygenerowany token:", wygenerowany_token)

token_do_weryfikacji = input("Podaj token do weryfikacji: ")
dane_uzytkownika = token.odczytaj_dane(token_do_weryfikacji)
if dane_uzytkownika is not None:
    print("Dane użytkownika:")
    print("Imię:", dane_uzytkownika[0])
    print("Nazwisko:", dane_uzytkownika[1])
    print("Adres e-mail:", dane_uzytkownika[2])
    print("Data ważności:", dane_uzytkownika[3])
else:
    print("Nieprawidłowy token")