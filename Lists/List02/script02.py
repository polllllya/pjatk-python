"""
Lista B - Lab3 - Zadanie 2
"""

# tworzenie listy 20 obiektów
lista = [i for i in range(20)]
print(lista)

# wyświetlanie tylko obiektów o indeksach będących liczbami pierwszymi
print("Obiekty o indeksach będących liczbami pierwszymi:")
print([lista[i] for i in range(2, len(lista)) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))])
