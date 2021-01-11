#Imagine you're writing the software for an inventory system for
#a store. Part of the software needs to check to see if inputted
#product codes are valid.
#
#A product code is valid if all of the following conditions are
#true:
#
# - The length of the product code is a multiple of 4. It could
#   be 4, 8, 12, 16, 20, etc. characters long.
# - Every character in the product code is either an uppercase
#   character or a numeral. No lowercase letters or punctuation
#   marks are permitted.
# - The character sequence "A1" appears somewhere in the
#   product code.
#
#Write a function called valid_product_code. valid_product_code
#should have one parameter, a string. It should return True if
#the string is a valid product code, and False if it is not.


#Add your code here!
def valid_product_code(code):
    trueOrnot = False
    code_count = 0
    num_count = 0
    j_count = 0
# sort uppercase and numbers
    for char in code:
        for j in char:
            j_count +=1
            if j.isupper():
                code_count += 1
            # finds if the letters are upper and there are numbers
            if j.isnumeric():
                num_count += 1
    # Checks to see if all letters and number are == to length of string
    if (num_count + code_count) == j_count:
    # Checks the divisible by 4 part
        if j_count % 4 == 0:
    # Looks for A1 in the string
            if (code.find('A1')) != -1:
                trueOrnot = True

    else:
        trueOrnot = False

    return trueOrnot













#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))
