story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

story_num = 0
text_num = 0
role_num = 0
dir_num = 0
cast_num = 0

if story == "A":
    story_num = 6

if story == 'B':
    story_num = 5

if story == 'C':
    story_num = 4

if story == 'D':
    story_num = 2


if text == 'A':
    text_num = 5

if text == 'B':
    text_num = 4

if text == 'C':
    text_num = 3

if text == 'D':
    text_num = 1

if role == 'A':
    role_num = 4

if role == 'B':
    role_num = 3

if role == 'C':
    role_num = 2

if role == 'D':
    role_num = 1

if director == 'A':
    dir_num = 3

if director == 'B':
    dir_num = 2

if director == 'C':
    dir_num = 1

if cast == 'A':
    cast_num = 2

if cast == 'B':
    cast_num = 1

result = story_num + text_num + role_num + dir_num + cast_num

print(result)

if result >= 20:
    print('Perfect score')

elif 17 <= result <= 19:
    print('Must do')

elif 14 <= result <= 16:
    print('Seriously consider')

elif 12 <= result <= 13:
    print('On the bubble')

elif result <= 11:
    print('pass')