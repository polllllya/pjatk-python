"""
Napisz skrypt, który dla trzech liczb a, b i c wprowadzonych z klawiaturysprawdza,
czy są to trójki pitagorejskie.Dodatkowo należy założyć, że a>0, b>0 oraz c>0
"""

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Wszystkie liczby muszą być większe od zera.")
else:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Podane liczby tworzą trójkę pitagorejską.")
    else:
        print("Podane liczby nie tworzą trójki pitagorejskiej.")