"""
Napisz funkcję sprawdzającą, które z podanych w argumncie liczb są liczbami doskonałymi.
Funckja możne przyjmować dowolną ilość arguemntów.
W wyniku działania funkcji powinien powstać słownik w postaci {liczba:True,liczba:False}
"""

def check_perfect_numbers(*numbers):
    result = {}
    for num in numbers:
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            result[num] = True
        else:
            result[num] = False
    return result

check_perfect_numbers(6, 12, 28, 7, 496, 8128)