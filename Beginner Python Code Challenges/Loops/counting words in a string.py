listOfStrings = ["this is a string",
                 "this is a string",
                 "this is also a string"]
numSpaces = 0

for currentString in listOfStrings:

    for currentCharacter in currentString:
        if currentCharacter == " ":
            numSpaces += 1
print(numSpaces)


