listOfStrings = ["Congratulations Huw Williams! "
                 "You are now enrolled in Computing in Python I:"
                 " Fundamentals and Procedural Programming."]
numspaces = 0

for currentString in listOfStrings:
    for currentChar in currentString:
        if currentChar == " ":
            numspaces += 1

numWords = numspaces + len(listOfStrings)
print("there are ", numspaces, " words in this list")



