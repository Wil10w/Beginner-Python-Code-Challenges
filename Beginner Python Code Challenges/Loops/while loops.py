x = 10
y = 20

while x < y:
    x += 1
    if x == 15:
        continue  # this if loop jumps over 15
    if x == 18:
        break
    print('x is ' + str(x))

     #to print '18' the print statement will need to sit below the 'continue statement.



