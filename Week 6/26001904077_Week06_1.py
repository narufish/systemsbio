"""
Created on 9/11/2021

@author: Alina Hazirah Ramlan
"""

import string, random, math

size = 20 # size of the initial condition
ruleNum = int(input("Wolfram rule number to be simulated (0~255):"))

#checks for valid input is entered in the rule number input
#range of valid input is 0~255
while ruleNum:
    if ruleNum>=0 and ruleNum<=255:
        break
    else:# if invalid input is entered, the user is asked to input again
        ruleNum = int(input("Please input a valid Wolfram rule number to be simulated (0~255):"))

#print("Please input the number of iterations:")
iterSize = int(input("Number of iterations:"))
#print("Random or non random initial condition: (1:Non-random, 2: random)")
randomSelect = int(input("Random or non random initial condition (1:Non-random, 2: random): "))


Rule90 = {"111":"0", "110":"1", "101":"0", "100":"1",
          "011":"1", "010":"0", "001":"1", "000":"0"}

# produces a binary string of the specified rule number (ruleNum)
wolfram_rule_string = "{0:{fill}8b}".format(ruleNum, fill="")
wolfram_rule_string = wolfram_rule_string.replace(" ","0") # ensures the zeros at the start are not empty

# creates a dictionary for the wolfram rule
wolfram_rule_dict = {"111":wolfram_rule_string[0], "110":wolfram_rule_string[1]
    , "101":wolfram_rule_string[2], "100":wolfram_rule_string[3]
    , "011":wolfram_rule_string[4], "010":wolfram_rule_string[5]
    , "001":wolfram_rule_string[6], "000":wolfram_rule_string[7]}
#print(wolfram_rule_dict)

#function to produce the a new layer from the intial/previous layer
def wolfram_fkt():
    x = ""
    for i in range(len(iterstr)-2):
        x+= wolfram_rule_dict[iterstr[i:i+3]]

    #adds a 0 at the front and the back of the result, so that the console output does not shrink
    x += "0"
    x = x.zfill(length)
    # display to better illustrate the Wolfram rule
    display = x.replace('1', 'X').replace("0","_") # replaces 0 with "_" and 1 with "X"

    print(display)
    return x

#function to produce a random binary string
def randomBinaryString(size):
    s = ""
    for i in range(size):
        num = random.randint(0,1)
        s += str(num)

    return s

# Checks for valid input for selecting random or non-random initial condition
while randomSelect:
    if randomSelect==1: #1:Non-random input (single 1 sandwiched between 0's)
        iterstr = "0" * math.floor(size / 2) + "1" + "0" * math.floor(size / 2)
        break
    elif randomSelect==2: #2:random input
        iterstr = randomBinaryString(size)
        break
    else: # asks the user to enter valid input when invalid input is entered
        print("Please enter a valid input (1:Non-random, 2:random):")
        randomSelect = int(input())


print(iterstr.replace('1', 'X').replace("0","_")) #print initial condition
length = len(iterstr) #size of initial condition string
#print(iterstr)

# called a certain number of times (iterSize) which results in the number of lines displayed
for i in range(iterSize):
    iterstr = wolfram_fkt()














