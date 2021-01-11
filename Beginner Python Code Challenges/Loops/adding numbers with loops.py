mystery_int = -7
answer = 0
if mystery_int > 0:
    for i in range(0, mystery_int + 1):
        answer = answer + i
else:
    for i in range(mystery_int, 0):

        answer = answer + i
print(answer)

