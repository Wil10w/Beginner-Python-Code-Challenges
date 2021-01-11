def word_count(string):
    c = ' '
    s = False
    count = 1
    try:
        for i in string:
            if i == ' ' and not s:
                count += 1
            if i == ' ':
                s = True
            else:
                s = False

        return count
    except:
        return 'Not a string'


print("Word Count:", word_count("Four  words are  here!"))
