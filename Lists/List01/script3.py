string1 = input('Enter the number in binary:\n' + 'bin = ')
string2 = input('Enter the number in octal:\n' + 'oct = ')
string3 = input('Enter the number in hexadecimal:\n' + 'hex = ')

number1 = int(string1, 2)
number2 = int(string2, 8)
number3 = int(string3, 16)
print()

print('The variable bin contains the number', bin(number1),
      'in binary, and when converted to decimal, the value is', number1)
print()

print('The variable oct contains the number', oct(number2),
      'in octal, and when converted to decimal, the value is', number2)
print()

print('The variable hex contains the number', hex(number3),
      'in hexadecimal, and when converted to decimal, the value is', number3)
