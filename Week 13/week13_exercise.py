import random

iter = 0 #number of iterations

file = open("textfile_week13.txt", "r") #read text file
Lines = file.readlines()# read the lines in the input text file

num_lines = len(Lines) #total number of lines
line_limit = num_lines-1 #randomization limit

counter = [5 for i in range(num_lines)] #counter values for each line

while len(Lines)>1:
    select = random.randint(0,line_limit) #generates random integer to select one of the lines
    counter = [i-1 for i in counter] #increments -1 for counter value for every line other than the selected line
    counter[select] +=2 # increments +1 for the counter value for the selected line

    # if the counter value for a line becomes 0, then delete that line
    for m,n in enumerate(counter):
        if n==0:
            del counter[m] #delete the counter value from the counter list
            del Lines[m] #delete the line from the lines list
            line_limit -= 1 #increment -1 from the randomization limit
    iter+=1 # indicate that an iteration had occured

# prints the final results
print("The final line is:")
for line in Lines:
    print(line)
print("Number of iterations: " + str(iter))
print("Final counter value: " + str(counter[0]))

# write the results into the output txt file
with open("newtextfile.txt", "w") as openWriteFile:
    openWriteFile.writelines(Lines)