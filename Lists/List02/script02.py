myList = []

print("Enter 20 numbers between −20 and 20")

while len(myList) < 20:
    myList.append(int(input("Enter an integer: ")))

print("List :", myList)
print()

print("Utwórz kopię listy:")

myListCopy = myList.copy()
print(myListCopy)
print()

print("Wyszukaj liczby pierwsze i utwórz z nich krotkę:")


def is_prime(n):
    # Sprawdza, czy liczba jest pierwsza
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(lst):
    # Zwraca listę liczb pierwszych na podstawie listy wejściowej
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    return primes


myTuple = tuple(get_primes(myListCopy))
print("List:", myListCopy)
print("Tuple:", myTuple)
print()

print("Podnieś do potęgi 2 liczby podzielne przez 2 i utwórz z nich krotkę:")


def do_degree(lst):
    degrees = []
    number = 2
    for i in lst:
        if (i % 2 == 0) and (number != 0):
            degrees.append(i ** 2)
            number -= 1
    return degrees


myTuple1 = tuple(do_degree(myListCopy))
print("List:", myListCopy)
print("Tuple:", myTuple1)
print()

print("4. Z pierwotnej listy wyszukaj liczby podzielne przez 2 i zamień je na literę  A")


def replace_with_letter(lst):
    replaced = []
    for i in lst:
        if i % 2 == 0:
            replaced.append("A")
        else:
            replaced.append(str(i))
    return replaced


myStringList = replace_with_letter(myListCopy)
print("List:", myListCopy)
print("Replaced by the letter A", myStringList)
