rating = "PG"
age = 8

if rating == 'G':
 print('You may see that movie!')


if rating == "PG":
 if age >= 8:
  print("You may see that movie!")
 else:
  print("You may not see that movie!")

if rating == "PG-13":
 if age >= 13:
  print("You may see that movie!")
 else:
  print('You may not see that movie!')

if rating == 'R':
 if age >= 17:
  print('You may see that movie!')
 else:
  print('You may not see that movie!')

if rating == 'NC-17':
 if age < 18:
  print('You may not see that movie!')
 else:
  print('You may see that movie!')