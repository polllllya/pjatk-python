"""
Zadanie 2 - Lista 2

Napisz skrypt, który będzie działał jak prosty kalkulator (obsługa dodawania, odejmowania, mnożenia, dzielenia, dzielenia bez reszty, %,
pierwiastek kwadratowy, pierwiastek dowolnego stopnia, potęga)
"""

import math

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

def dzielenie_bez_reszty(a, b):
    return a // b

def modulo(a, b):
    return a % b

def pierwiastek_kwadratowy(a):
    return math.sqrt(a)

def pierwiastek_stopnia(a, stopien):
    return a ** (1 / stopien)

def potega(a, b):
    return a ** b


def wybierz_operacje():
    print("Prosty kalkulator")
    print("Dostępne operacje:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Dzielenie bez reszty")
    print("6. Modulo")
    print("7. Pierwiastek kwadratowy")
    print("8. Pierwiastek dowolnego stopnia")
    print("9. Potęga")

    wybor = input("Wybierz numer operacji (1-9): ")
    return wybor


def wczytaj_liczby():
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    return liczba1, liczba2


def oblicz_operacje(wybor, liczba1, liczba2):
    if wybor == '1':
        return dodawanie(liczba1, liczba2)
    elif wybor == '2':
        return odejmowanie(liczba1, liczba2)
    elif wybor == '3':
        return mnozenie(liczba1, liczba2)
    elif wybor == '4':
        return dzielenie(liczba1, liczba2)
    elif wybor == '5':
        return dzielenie_bez_reszty(liczba1, liczba2)
    elif wybor == '6':
        return modulo(liczba1, liczba2)
    elif wybor == '7':
        return pierwiastek_kwadratowy(liczba1)
    elif wybor == '8':
        stopien = int(input("Podaj stopień pierwiastka: "))
        return pierwiastek_stopnia(liczba1, stopien)
    elif wybor == '9':
        return potega(liczba1, liczba2)
    else:
        return None


wybor = wybierz_operacje()
liczba1, liczba2 = wczytaj_liczby()
wynik = oblicz_operacje(wybor, liczba1, liczba2)

if wynik is not None:
    print("Wynik:", wynik)
else:
    print("Nieprawidłowy wybór operacji.")
