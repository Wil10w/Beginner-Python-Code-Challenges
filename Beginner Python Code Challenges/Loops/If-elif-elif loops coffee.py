cafe = "Octane"
balance = 5.5

price = 0
# the loops below determine which cafe and stores the preset
# price in the variable 'price'
if cafe == 'Octane':
    price = 6

elif cafe == 'Galloway':
    price = 5


elif cafe == 'Starbucks':
    price = 4


elif cafe == 'Revelator':
    price = 3


elif cafe == 'Dunkin':
    price = 2


# now we determine if the coffee can be bought at the cafe

if balance >= price:
    print('With ' + str(balance) + ' dollars, I can buy coffee at ' + cafe)
elif balance < price:
    print('With ' + str(balance) + ' dollars, I cannot buy coffee at ' + cafe)
