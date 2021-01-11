mystery_list = ["Taylor Swift", "Twenty Two", "Georgia Tech"]
myst_letter1 = "t"
myst_letter2 = "T"

num_letter = 0

for string in mystery_list:

    for word in string:
        if word == "t":
            num_letter += 1
        if word == "T":
            num_letter += 1
print(num_letter)