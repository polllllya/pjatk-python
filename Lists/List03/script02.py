"""
Lista B - Lab4 - Zadanie 2
"""


liczba = input("Podaj liczbę: ")
z_systemu = int(input("Podaj system liczbowy liczby wejściowej (2, 8, 10, 16): "))
do_systemu = int(input("Podaj system liczbowy docelowy (2, 8, 10, 16): "))


if z_systemu == 2:
    dziesietna = int(liczba, 2)
elif z_systemu == 8:
    dziesietna = int(liczba, 8)
elif z_systemu == 10:
    dziesietna = int(liczba)
elif z_systemu == 16:
    dziesietna = int(liczba, 16)
else:
    print("Niepoprawny system liczbowy")
    exit()


if do_systemu == 2:
    wynik = bin(dziesietna)[2:]
elif do_systemu == 8:
    wynik = oct(dziesietna)[2:]
elif do_systemu == 10:
    wynik = str(dziesietna)
elif do_systemu == 16:
    wynik = hex(dziesietna)[2:]
else:
    print("Niepoprawny system liczbowy")
    exit()

print("Wynik:", wynik)