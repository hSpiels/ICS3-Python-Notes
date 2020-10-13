

word ="elephant"

blanks= "_"*len(word)

print(word)
print(blanks)


# for letter in word:
#     print(letter)
#     if letter = userGuess
    

for i in range( len(word)):
    print(i, word[i], blanks[i])
    if word[i] == userinput:
        blanks[i]
    
def replaceLetter(stringIn, index, letter):
    return stringIn[:index] + letter + stringIn[index + 1:]

print (replaceLetter(word, 3, 'z'))

