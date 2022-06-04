import random
import string


def randomword3(length):
    # creates the set of lowercase ASCII characters plus the additional symbols
    s = list(string.ascii_lowercase) + ['.',';']

    # generates a random number from the range of the previous set to be used as the index
    n = random.randint(0, len(s)-1)
    # selects a character from the character set at the generated index number and initializes the output
    out = s[n]

    while (len(out) < length):  # the loop continues until specified length is reached
        # generates a random number from the range of 0 to the size of the character set
        # to be used as the index for selection
        n = random.randint(0, len(s)-1)
        # selects a character from the character set at the generated index number and attaches it the the output
        out = out + s[n]

    return out


#print(randomword3(10))