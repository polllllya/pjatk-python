import random

wybor = input("Wybierz opcję: (1) wprowadź liczby samodzielnie, (2) wygeneruj losowe liczby: ")

if wybor == "1":
    liczby = []
    for i in range(20):
        liczba = int(input(f"Wprowadź liczbę {i+1}: "))
        while liczba < 1 or liczba > 100:
            liczba = int(input("Liczba musi być z zakresu 1-100. Spróbuj jeszcze raz: "))
        liczby.append(liczba)
elif wybor == "2":
    liczby = [random.randint(1, 100) for i in range(20)]
else:
    print("Nieprawidłowa opcja.")
    exit()

print("Wygenerowane liczby:")
print(liczby)