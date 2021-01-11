# I removed the vowels by looping and removing any letters in the 'vowels' list

def disemvowel(string):
    vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
    for letter in string:
        if letter in vowels:
            string = string.replace(letter, '')

    return string




print(disemvowel("This website is for losers LOL!"))