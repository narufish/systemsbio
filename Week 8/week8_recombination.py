import random
import string

# function with combines the dna sequences at a random position
def recombination(dna1,dna2):
    pos = random.randint(0,len(dna1))
    newdna1 = dna1[:pos] + dna2[pos:]
    newdna2 = dna2[:pos] + dna1[pos:]
    return newdna1,newdna2

# generate a random dna sequence (ascii letters)
def generateDNA(size):
    dna = ''
    for i in range(size):
        dna += random.choice(string.ascii_letters)

    return dna

a = generateDNA(10)
b = generateDNA(15)

print("first dna: ",a)
print("second dna: ",b)
print()

c,d = recombination(a,b)
print("recombined first dna: ",c)
print("recombined second dna: ",d)