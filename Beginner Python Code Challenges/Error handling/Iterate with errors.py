given_items = ["one", "two", 3, 4, "five", ["six", "seven", "eight"]]

for item in given_items:
    try:
        for j in item:
            print(j)
    except TypeError:
        print('Not iterable')
        pass
