import random
import string
import numpy as np

#Reading files to populate list  of dieases and list of past antibodies
# list of diseases
with open("AISdieases.txt","r") as loadDiseases:
    listOfDiseases = loadDiseases.read().split(",")

with open("AISdieases.txt","r") as loadMemoryCell:
    memoryCell = loadMemoryCell.read().split(",")

#Set global variables
antigen = random.choice(listOfDiseases)
antigenLength = len(antigen)
antibodyNumber = 200
generations = 20
mutationChance = 10
selectPenalty = 2
memoryCellFraction = 10

# Generates a random gene out of all printable ASCII characters
def randomGene():
    return random.choice(string.printable)

# Creates antibodyNumber-number of antibodies with random genes
def initialAntibodyPopulation():
    initPop = []
    for i in range(antibodyNumber):
        initPop.append(''.join(random.choice(string.printable) for i in range(antigenLength)))
    return initPop

# The affinity value, how well on antibody fits the antigen (here again as penalty)
def affinityPenaltyMetric(antibodyAttack):
    for i in range(len(antibodyAttack)):
        false += abs(ord(competingDNA[i]) - ord(target[i]))
    return false
    # MY CODE

def weightedAntibodyChoice(listOfAntibodyAffinity):
    probs = [listOfAntibodyAffinity[i][1] for i in range(len(listOfAntibodyAffinity))]
    probs = np.array(probs)
    probs /= probs.sum()
    return listOfAntibodyAffinity[np.random.choice(len(listOfAntibodyAffinity), 1, p = probs)[0]][0]

# Mutation of single antibody in 1/mutationRatio chance
def mutation(antibodyMutate, mutationRatio):
    mutatedDNA = ""
    for gene in range(antigenLength):
        mutationCheck = random.randint(0, mutationRatio)
        if mutationCheck == 1:
            mutatedDNA += randomGene()
        else:
            mutatedDNA += antibodyMutate[gene]
        return mutatedDNA

currentAntibodyPopulation = initialAntibodyPopulation()

for ik in memoryCell:
    if len(ik) == len(currentAntibodyPopulation[memoryCell.index(ik)]):
        currentAntibodyPopulation[memoryCell.index(ik)] = ik

for i in range(generations):
    lastAffinityArray = []
    for k in currentAntibodyPopulation:
        lastAffinityArray.append(affinityPenaltyMetric(k))

    print("The antibody closest to the antigen at iteration", i, "is ---",
          currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))],
          "--- with penalty:", min(lastAffinityArray))

    # Returns an antibody list with their respectie affinity in format
    # [["antibody1", affinity], ["antibody2", affinity2][...]...]
    populationWeighted = []
    for individual in currentAntibodyPopulation:
        individualPenalty = affinityPenaltyMetric(individual)
        if individualPenalty == 0:
            antibodyFitnessPair = (individual, 1.0)
        else:
            antibodyFitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(antibodyFitnessPair)

    # New set repopulated with newly selected and mutated ntibodies
    currentAntibodyPopulation = []
    for m in range(int(antibodyNumber/2)):
        #Random selection, weighted by affinity (higher affinity == higher probability)
        bestAntibody1 = weightedAntibodyChoice(populationWeighted)
        bestAntibody2 = weightedAntibodyChoice(populationWeighted)

        # Mutation in 1/mutationChance chances
        bestAntibody1 = mutation(bestAntibody1, mutationChance)
        bestAntibody2 = mutation(bestAntibody1, mutationChance)

        # Combining the list of antibodies for next iteration
        currentAntibodyPopulation.append(bestAntibody1)
        currentAntibodyPopulation.append(bestAntibody2)

lastAffinityArray = []
for g in currentAntibodyPopulation:
    lastAffinityArray.append(affinityPenaltyMetric(g))

with open("AISmemoryCell.txt", "r") as loadMemoryCell:
    newMemoryCell = loadMemoryCell.read()

if min(lastAffinityArray) < 50:
    putIntoMemory = currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))]
    #Prints fittest antibody out of the resulting list
    print("Fittest String at", generations, "is:", putIntoMemory)
    newMemoryCell += "," + putIntoMemory
    with open("AISmemoryCell.text") as writeMemoryCell:
        writeMemoryCell.write(newMemoryCell)
else:
    putIntoMemory = ""
    print("No antibody to put into memory")

del memoryCell
del listOfDiseases













