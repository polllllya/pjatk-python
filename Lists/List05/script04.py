"""
Napisz funkcję korzystającą z wyrażeń lambda.
Funkcja powinna-wypisywać N liczb podzielnych przez 2, ale nie podzielnych przez 3-umożliwić sorotwanie liczb rosnąco i malejąco
"""


def divisible_by_2_not_3(n, reverse=False):
    numbers = filter(lambda x: x % 2 == 0 and x % 3 != 0, range(2, n * 2 + 1))
    numbers_sorted = sorted(numbers, reverse=reverse)
    for number in numbers_sorted[:n]:
        print(number)


divisible_by_2_not_3(5)
print()
divisible_by_2_not_3(5, reverse=True)
