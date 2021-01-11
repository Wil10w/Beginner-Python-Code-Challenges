mystery_string = "Hello! What a fine day it is today."
mystery_character = "a"

num_letters = 0

for i in mystery_string:

    for j in i:
        if j == mystery_character:
            num_letters += 1

print(num_letters)

# First, we're counting something, so we start by initializing
# a counter to 0:
count = 0

# Now, we want to iterate through each character in mystery_string.
# We can do that with this loop:
for a_character in mystery_string:

    # Next, we want to compare the current character in the string
    # to mystery_character to see if they're the same.
    if a_character == mystery_character:
        # If so, we add to the counter:
        count += 1

# Then, at the end, we print the counter:
print(count)