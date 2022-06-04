import random
import string


def randomword3(length):
    # creates the set of lowercase ASCII characters, plus the additional characters/symbols
    s = list(string.ascii_lowercase) + ['.',';']

    # add the odd characters to the list again to increase the selection probability by twice its original probability
    for i in range(len(s)//2):
        s.append(s[2*i]) # 2*n ensures only the odd characters are appended, up until half the length of the list
        # first character index is 0, second character index is 2, third character index is 4,...

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