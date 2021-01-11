def lucky_sevens(string):
    sevens = 0
    outcome = False
    for i in string:
        if i == '7':
            sevens += 1
            if sevens == 3:
                outcome = True

            else:
                outcome = False
    return outcome

print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))