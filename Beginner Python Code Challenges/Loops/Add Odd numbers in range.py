mystery_int = 50

result = 0
for i in range(1, mystery_int):
    if i % 2 != 0:
        result += i

print(result)