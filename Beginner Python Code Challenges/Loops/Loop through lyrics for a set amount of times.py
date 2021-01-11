lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

# This code is looping though each " " (line of lyrics) for the amount of times written in
# Lines_of_sanity

# the main struggle was breaking the loop at the right time - I was getting results of 8 lines
# instead of 6.

# this was fixed with a further nested loop with a check for zero and a break command.

while lines_of_sanity != 0:
    for lines in lyrics:
        if lines_of_sanity == 0:
            break
        lines_of_sanity -= 1
        print(lines)