def is_leap_year(your_year):
    leap_year = True
    if (your_year % 4) ==0 and (your_year % 100) != 0:
        leap_year = True
    elif your_year % 400 == 0:
        leap_year = True
    elif (your_year % 100) == 0:
        leap_year = False
    else:
        leap_year = False
    return leap_year

print("1993 is a leap year:", is_leap_year(1993))
print("1996 is a leap year:", is_leap_year(1996))
print("1900 is a leap year:", is_leap_year(1900))
print("2000 is a leap year:", is_leap_year(2000))
