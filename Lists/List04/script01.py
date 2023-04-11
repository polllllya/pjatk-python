"""
Lista B - Lab5 - Zadanie 1
"""

klucz = int(input("Podaj klucz szyfru Cezara (liczba całkowita): "))
operacja = input("Co chcesz zrobić? 'szyfruj' czy 'deszyfruj'? ")
tekst = input("Podaj tekst do zaszyfrowania/deszyfrowania: ")

wynik = ''
alfabet = 'abcdefghijklmnopqrstuvwxyz'
ALFABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if operacja == 'szyfruj':
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                indeks = ord(znak) - ord('A')
                indeks = (indeks + klucz) % 26
                wynik += ALFABET[indeks]
            else:
                indeks = ord(znak) - ord('a')
                indeks = (indeks + klucz) % 26
                wynik += alfabet[indeks]
        else:
            wynik += znak
elif operacja == 'deszyfruj':
    klucz = -klucz
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                indeks = ord(znak) - ord('A')
                indeks = (indeks + klucz) % 26
                wynik += ALFABET[indeks]
            else:
                indeks = ord(znak) - ord('a')
                indeks = (indeks + klucz) % 26
                wynik += alfabet[indeks]
        else:
            wynik += znak

print("Wynik:", wynik)
