import math
#   I have little understanding of the math, but the challenge was catching the ValueError and
#   returning the False outcome.

def is_square(n):
    try:
        root = math.sqrt(n)

        if int(root + 0.5) ** 2 == n:
            if n < 0:
                return False
            else:
                return True

        else:
            return False

    except ValueError:
        return False


print(is_square(-2))
