"""
Lab09 - wyjątki
"""

def pobierz(sek,ind):
    return sek[ind]

pliki = ["czarny_kot.txt", "nowy_plik.txt"]
ind = 1

try:
    print(pobierz(pliki,ind))
except IndexError:
    print("Wystapil blad")


try:
    print(pobierz(pliki,ind))
except IndexError as e:
    print("Wystapil blad: ",e)
else:
    print("Pobrane")


pliki = ["czarny_kot.txt", "nowy_plik.txt"]
ind = 1

try:
    p = pobierz(pliki,ind)
    print(p)
    f = open(p)
except (IndexError, FileNotFoundError) as e:
    print("Wystapił blad: ",e)
else:
    print("Pobrane")