"""
Napisz skrypt wyświetlający wszystkie liczby całkowite z przedziału od 20 do 80 podzielne przez dowolną liczbę k,
którą podaje użytkownik. Liczby powinny być wyświewtlone w postaci listy lub słownika. Decyduje użytkownik skryptu.
"""

k = int(input("Podaj liczbę k >> "))

lista = []
for i in range(20, 81):
    if i % k == 0:
        lista.append(i)

sposob = input("W jaki sposób chcesz wyśwetlić liczby?"
               "\n1. Lista - napisz \"lista\""
               "\n2. Słownik - napisz \"słownik\""
               "\n>> ")

if sposob == "lista":
    print(lista)

if sposob == "słownik":
    slownik = {i: lista[i] for i in range(len(lista))}
    for key, value in slownik.items():
        print(key, "-", end=" ")
        print(value)