years = 0
months = 1
days = 0

if years >= 4:
 print("dog")

elif years == 1 or years <= 4 and not years <= 0:
 print("watch")


elif months >= 6 or years == 1:
 print("concert tickets")

elif days >= 1 or months <= 6 and not months <= 0:
 print("candy")

else:
 if years == 0 and months == 0 and days == 0:
  print("yacht")