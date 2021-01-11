beats_per_measure = 4
measures = 5
current_measure = 0

for i in range(1,measures + 1):
    current_measure += 1
    print(current_measure)
    for j in range(2,beats_per_measure + 1):
        print(j)