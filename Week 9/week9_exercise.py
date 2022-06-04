'''
@author: Alina Hazirah Ramlan
18/11/2021
'''

import random
import string
import numpy as np

target = "Alina Hazirah" # string (dna) that the algorithm tries to achieve
dnaLength = len(target) #length of the dna (string)
populationSize = 20 #number of possible solutions for each generation
generations = 10000 # maximum number of generations for the GA
mutationChance = 50 # determines the probability for each gene in every dna to mutate #100
# probability = 1/mutationChance
f_num = 2


# function that returns a random ascii character to be added to the mutated gene
def randomGene():
    return random.choice(string.printable)

# function that generates generation 0 for the algorithm
# every string (dna sequence) is randomly generated in the initial generation
# the random dna samples are generated up to a certain number (populationSize)
def initialPopulation():
    initPop = []
    for i in range(populationSize):
        initPop.append(''.join(random.choice(string.printable) for i in range(dnaLength)))
    return initPop

# fitness function is the main determinant for the selection process
# this process is ignored for now
def fitnessFunction(competingDNA,f_num):
    #Calculate Levenshtein distance of the competingDNA to the target
    #the greater the fitness function the greater the penalty given to the specific character
    false = 0

    # 1/fitness = |x-y|
    if f_num==1:
        for i in range(len(competingDNA)):
            false += abs(ord(competingDNA[i])-ord(target[i]),2)

    # 1/fitness = (x-y)^2
    if f_num == 2:
        for i in range(len(competingDNA)):
            false += pow(ord(competingDNA[i])-ord(target[i]),2)

    # 1/fitness = (x!=y) ? fitness+=1:0
    if f_num == 3:
        for i in range(len(competingDNA)):
            if competingDNA[i]!=target[i]:
                false += 1

    # The probability of each competingDNA in a population will have the penalty = 1/fitness
    # the greater the fitness the less its probability/weight is
    fitness = false
    return fitness

# function that has a 1/mutationRatio chance of mutating each gene in a string(dna sequence)
def mutation(competingDNA, mutationRatio):
    mutatedDNA = ""
    # every gene has a chance of 1/mutationRation chance of mutating
    for i in range(len(competingDNA)):
        new_gene = randomGene() # new mutated gene (random ascii character) is generated for each gene
        # random integer,a, determines if the gene will be mutated
        # probability to be mutated = 1/mutationRatio
        a = random.randint(0, mutationRatio)

        # we let the random number that mutates the dna to be 7, this can be changed to any integer from 0 to mutationRatio
        # if this number gets picked, then mutate the single character (gene) and add it to the mutatedDNA string
        if a==7:
            mutatedDNA += new_gene
        # otherwise, the original character is added to the mutatedDNA string
        else:
            mutatedDNA+= competingDNA[i]

    return mutatedDNA

# function that performs recombination at a random position(gene) on the string (dna sequence)
def recombination(competingDNA1, competingDNA2):
    #the position is randomly generated within the range of 0 to the size of the dna 1(competingDNA1)
    pos = random.randint(0, len(competingDNA1))
    # Both dna 1 and 2 is cut at the random gene(pos), and the ends are switched between them
    DNAout1 = competingDNA1[:pos] + competingDNA2[pos:]
    DNAout2 = competingDNA1[:pos] + competingDNA2[pos:]
    # the new dna 1 and 2 is a crossover of the switched ends

    return (DNAout1, DNAout2)

def weightedDNAchoice(competingDNAfitnessPairs):
    #print("competingDNAfitnessPairs:", competingDNAfitnessPairs)
    probs = [competingDNAfitnessPairs[i][1] for i in range(len(competingDNAfitnessPairs))]
    #print("Probabilities:", probs)
    probs = np.array(probs)
    probs /= probs.sum()
    #print("Normalized Probabilities", probs)
    #print(competingDNAfitnessPairs[np.random.choice(len(competingDNAfitnessPairs), 1, p = probs)[0]][0])
    return competingDNAfitnessPairs[np.random.choice(len(competingDNAfitnessPairs), 1, p = probs)[0]][0]

# Initializes generation 0 (initial generation)
currentPopulation = initialPopulation()
# loop to generate the next generation (done until max number of generations is reached)
for i in range(generations):
    lastfitnessarray = []
    for k in currentPopulation:
        lastfitnessarray.append(fitnessFunction(k,f_num))
    #Prints the generation number and its current fittest DNA string
    print("The fittest DNA for generation", i, "is ---", currentPopulation[
        lastfitnessarray.index(min(lastfitnessarray))],
          "--- with penalty:", min(lastfitnessarray))
    #Returns a new population with their respective fitness in format
    # [["dnastr1",penalty1],["dnastr2", penalty2],[...]...]
    populationWeighted = []
    for individual in currentPopulation:
        individualPenalty = fitnessFunction(individual)
        if individualPenalty == 0:
            DNAfitnessPair = (individual, 1.0)
        else:
            DNAfitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(DNAfitnessPair)

    best_fit = currentPopulation[lastfitnessarray.index(min(lastfitnessarray))]
    # Reset population and repopulate with newly selected, recombined, and mutated DNA
    currentPopulation = []
    for m in range(int((populationSize/2))-1):
        fittestDNA1 = weightedDNAchoice(populationWeighted)
        fittestDNA2 = weightedDNAchoice(populationWeighted)
        #Recombination or crossover
        fittestDNA1, fittestDNA2 = recombination(fittestDNA1,fittestDNA2)
        #Mutation in 1/mutationChance chances
        fittestDNA1 = mutation(fittestDNA1, mutationChance)
        fittestDNA2 = mutation(fittestDNA2, mutationChance)
        # Combining the population for next iteration
        currentPopulation.append(fittestDNA1)
        currentPopulation.append(fittestDNA2)
    # include a pair of the best samples from previous generation to the next one
    currentPopulation.append(weightedDNAchoice(populationWeighted))
    currentPopulation.append(weightedDNAchoice(populationWeighted))


# Creates an array of penalty value for each DNA in population
lastfitnessarray = []
for g in currentPopulation:
    lastfitnessarray.append(fitnessFunction(g,f_num))
# Prints fittest DNA out of the resulting population
print("Fittest String at", generations, "is:",
      currentPopulation[lastfitnessarray.index(min(lastfitnessarray))])


















