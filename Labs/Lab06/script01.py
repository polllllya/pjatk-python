"""
Lab06 - Funkcje
"""
print("Funkcje proste")

def show(a, b):
    print(a, b)


def add(a, b):
    return a + b


show(2, 4)

print("---------------------------")

c = add(5, 6)
print(c)

print("---------------------------")

print("Funkcje wewnetrzne")

def fun1(a):
    print(a)

    def fun2():
        print(a * 2)

    fun2()


fun1(5)

print("---------------------------")


def count(a, b):
    print(a * b)


# aljas -> referencja
test = count
test(2, 4)
