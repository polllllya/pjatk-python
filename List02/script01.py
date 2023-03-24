name = input("Name: ")
birthday = input("Birthday: ")
email = input("Email: ")
number = input("Number: ")

print()

# List[we can only store one type of data, but we can modify it]
myList = [name, birthday, email, number]
print(myList)

print()

# Tuple[we may store different types of data, but we cannot modify this data]
myTuple = (name, birthday, email, int(number))
print(myTuple)

print()


# Dictionary[ are used to store data values in key:value pairs]
myDict = {"Name": name, "Birthday": birthday, "Email": email, "Number": number}
print(myDict)
print(myDict["Name"])
