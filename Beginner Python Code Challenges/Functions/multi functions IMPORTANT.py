def word_count(a_string):
    count = 1
    for i in a_string:
        if i == ' ':
            count += 1
    return count


def letter_count(a_string):
    count = 0
    for i in a_string:
        count += 1
        if i == ' ':
            count -= 1

    return count


def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)


a_string = "Up with the white and gold"

print(average_word_length(a_string))