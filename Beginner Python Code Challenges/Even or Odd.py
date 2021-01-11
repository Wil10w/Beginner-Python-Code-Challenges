# A simple program to find out if the integer is odd or even

def even_or_odd(number):
    # determining is even by seeing if it is divisible by 2
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(even_or_odd(3))
