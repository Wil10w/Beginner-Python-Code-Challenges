mystery_string = "Lucy"
length = len(mystery_string)

for row in range(length):
    for column in range(row + 1):
        print(mystery_string[column], end="")
    print()