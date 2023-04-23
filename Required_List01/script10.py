"""
Napisz skrypt, który korzystając z instrukcji while, sumuje liczby nieparzyste w przedziale od 1 do 100
"""

i = 1
suma = 0

while i <= 100:
    if i % 2 != 0:
        suma += i
    i += 1

print("Suma liczb nieparzystych od 1 do 100 wynosi:", suma)