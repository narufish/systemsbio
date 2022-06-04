
class Ant:
    '''
    colonyName/hiveName - string that specifies name of the colony the ant belongs to
    location - (x,y) coordinates of the ant in the screen
    state - integer that describes if ant is dead(0) or alive(1)
    food_cost - cost/pheromones for path to food at ants current position from the colony location
    species - string that describes type of
    '''

    def __init__(self,colonyName,location,state=1,food_cost=0,species=0):
        self.species = antSpecies[species]
        self.colonyName = colonyName
        self.location = location
        self.state = state
        self.food_cost = food_cost

class Bee:
    def __init__(self,hiveName,location,state=1,food_cost=0,species=0):
        self.species = beeSpecies[species]
        self.hiveName = hiveName
        self.location = location
        self.state = state
        self.food_cost = food_cost

antSpecies = ["larger worker", "small worker", "queen", "soldier"]
beeSpecies = ["worker", "laying worker", "drone", "queen"]

ant1 = Ant("ant farm", (2,3),1,0,0)
ant2 = Ant("ant farm", (3,3),1,0,1)
ant3 = Ant("ant farm", (2,3),1,0,2)

bee1 = Bee("bee farm", (2,3),1,0,0)
bee2 = Bee("bee farm", (2,3),1,0,1)
bee3 = Bee("bee farm", (2,3),1,0,2)


print("Species of ant1 is " + ant1.species)
print("Species of ant2 is " + ant2.species)
print("Species of ant3 is " + ant3.species)
print()

print("Species of bee1 is " + bee1.species)
print("Species of bee2 is " + bee2.species)
print("Species of bee3 is " + bee3.species)



