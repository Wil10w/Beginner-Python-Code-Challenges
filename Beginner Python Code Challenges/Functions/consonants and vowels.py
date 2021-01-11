def count_letters(string, buul):
    counter = 0
    conson = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    if buul is True:
        for letters in string:
            for chars in conson:
                if letters == chars:
                    counter +=1



    if buul is False:
        for letters in string:
            for chars in vowels:
                if letters == chars:
                    counter += 1

    return counter






a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))