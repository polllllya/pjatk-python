"""
Zadanie 1 - Lista 2

Napisz skrypt, który pobierze od użytkownika 3 liczby całkowite i w odpowiedzi na ekranie wyświetli
liczbę gwizdek, # i $. Każdy znak to osobna kolumna. Zastosuje odpowiednie formatowanie.

*   #   $
*   #   $
*   #   $
*   #
*
*
"""

number1 = int(input("Podaj pierwszą liczbę całkowitą: "))
number2 = int(input("Podaj drugą liczbę całkowitą: "))
number3 = int(input("Podaj trzecią liczbę całkowitą: "))

max_number = max(number1, number2, number3)

for i in range(max_number):
    column1 = "*" if i < number1 else " "
    column2 = "#" if i < number2 else " "
    column3 = "$" if i < number3 else " "
    print("{:^5} {:^5} {:^5}".format(column1, column2, column3))