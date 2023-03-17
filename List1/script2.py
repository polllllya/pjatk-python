word1 = input('Enter the 1 word: ')
word2 = input('Enter the 2 word: ')

print("Now:", word1, word2)

word1 = word1.replace("o", "7").replace("a","7").replace("u","7").replace("e","7").replace("i","7")

# I didn't do for all the consonantal letters, but for most
word2 = word2.replace("b","6").replace("d","6").replace("f","6").replace("h","6").replace("k","6").replace("l","6")\
    .replace("c","6").replace("n","6").replace("p","6").replace("s","6").replace("t","6").replace("z","6")\
    .replace("q","6").replace("w","6").replace("r","6").replace("g","6").replace("x","6").replace("m","6")

word = (word1 + word2).upper()
print('After replace:', word)
