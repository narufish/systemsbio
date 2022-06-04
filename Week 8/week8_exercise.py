import random
import string

# generate a random dna sequence (ascii letters)
def generateDNA(size):
    dna = ''
    for i in range(size):
        dna += random.choice(string.ascii_letters)
    return dna

# mutation function
def mutateString(dna):
    #for every gene in the dna, there is 1/100 chance of mutating the each gene in the dna sequence
    for i in range(len(dna)):
        new_gene = random.choice(string.ascii_letters)#new gene is generated
        a = random.randint(1,100)

        if a==17:
            dna = dna[:i] + new_gene + dna[i + 1:]
    return dna

# generate a random string of ascii letters sequence, with size = 10
a = generateDNA(10)
print("Initial DNA (Generation 0)",a)

print("Mutation:")

for i in range(10):

    a = mutateString(a)
    print("Generation", i+1,": ",a)

