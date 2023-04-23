"""
Zmodyfikuj zadanie 7 w taki sposób aby użytkownik mógł podać zakres liczb oraz ilość dowolnych liczb k.
Wyniki wyświetl w postaci słownika (k: liczby całkowite)
"""

start = int(input("Podaj wartość początkową przedziału: "))
end = int(input("Podaj wartość końcową przedziału: "))

k_lista = []
k_input = input("Podaj wartości liczb k, oddzielone spacjami: ")
for val in k_input.split():
    k_lista.append(int(val))

result = {}
for k in k_lista:
    result[k] = [x for x in range(start, end+1) if x % k == 0]

print(result)