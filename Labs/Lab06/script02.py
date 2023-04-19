'''
Lab06 - argumenty funkcji
'''


def show(a, b, c):
    print(a, b, c)


show(3, 4, 5)
show(a=0, c=8, b=3)

print("Przykład 2")


def show2(a, b=4, c=8):
    print(a, b, c)


show2(2)
show2(1, 2)
show2(3, c=6)

print("Argumenty dowolne")
show(1, 3, 45)


def show(*arg):
    print(arg)


def show3(**arg):
    print(arg)


show3(a=2, b=3, c=4)

print("Przekazywaniie elementów(słowo kluczowe")


def show4(a, b, *args, c):
    print(a, b, *args, c)

show4(1, 2, 3, 4, c=5)
