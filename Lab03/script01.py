"""
Lab03 - Listy
"""

# Tworzenie list
list1 = []
print(list1)

list1 = [1, 2, 3]
print(list1)

list2 = [6, 9, 2]
print(list1)

list3: list[int] = [4, 6, 7]
print(list3)

# int float string
list4 = [1, 4.7, "cos"]
print(list4)

word = "bhgegdfeg"
list5 = list(word)
print(list5)

# Indeksowanie listy
print(list5[0])
print(list5[1:])
# print(list5[-1])
print(list5[0:2])
print(list5[::2])
print(list5[0:-1:2])
print(list5[::-1])
print(list1[len(list1) - 1])  # rozmiar

matrix = [1, 2, [3, 4]]
print(matrix[2][0])

# Modyfikowanie
list1.append(7)
print(list1)

list1.insert(1, 4)
print(list1)

list4.remove("cos")
print(list4)

list4.pop()
print(list4)

list4.pop(0)
print(list4)

# Lączenie list
list12 = list1 + list2
print(list12)

list6 = list1 + [8, "cos", 4]
print(list6)

list3.append(3.14)
print(list3)

list1.append(list3)
print(list1)

list1 = list1 * 3
print(list1)

list2.extend(list3)
print(list2)

list2.sort(reverse=True)
print(list2)

listA = list1
print(listA)
print(list1)

list1.pop()
print(list1)
print(listA)

listB = list1.copy()
print(listB)

listB.pop()
print(listB)
