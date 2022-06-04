import random
import numpy as np

def errorFunction(x):
    return sum([50*np.sin(x[i]) + x[i]**2 + 100 for i in range(len(x))])

# a class of a computer agent, here also called "particle"
class individualParticle:
    def __init__(self, x0):
        self.individualPosition = []
        self.individualVelocity = []
        self.individualBestPosition = []
        self.individualBestError = -1
        self.individualError = -1

        #Initializes the starting position and velocity of each particle
        for i in range(0, numStartingLocation):
            self.individualVelocity.append(random.uniform(-1,1))
            self.individualPosition.append(x0[i])

    # Evaluate the current fitness of the computer agents
    def evaluate(self, costFunction):
        self.individualError = costFunction(self.individualPosition)

        # The current position of the agent is compared with the individual best and updated if necessary
        if self.individualError < self.individualBestError or self.individualBestError == -1:
            self.individualBestPosition = self.individualPosition
            self.individualBestError = self.individualError

    # Calculate the new agent's velocity
    def update_velocity(self, groupsBestPosition):
        #The parameters w,c1, and c2 are changed to
        w = 1.0     # Inertia weight of previous velocity
        c1 = 2.0      # Cognitive constant (distance from the individual's known best position)
        c2 = 1.0      # Social constant (distance from the group's known best position)

        # Random numbers to compensate for the cognitive and social constants
        for i in range(0, numStartingLocation):
            r1 = random.random()
            r2 = random.random()
            # Updating cognitive velocity and social velocity
            cognitiveVelocity = c1 * r1 * (self.individualBestPosition[i] - self.individualPosition[i])
            socialVelocity = c2 * r2 * (groupsBestPosition[i] - self.individualPosition[i])
            self.individualVelocity[i] = w * self.individualVelocity[i] + cognitiveVelocity + socialVelocity

    # Update the position of each agent based on the new velocity updates
    def positionUpdate(self, bounds):
        for i in range(0, numStartingLocation):
            self.individualPosition[i] = self.individualPosition[i] + self.individualVelocity[i]
            # Compensate maximum position?
            if self.individualPosition[i] > bounds[i][1]:
                self.individualPosition[i] = bounds[i][1]
            # Compensate minimum position?
            if self.individualPosition[i] < bounds[i][0]:
                self.individualPosition[i] = bounds[i][0]

# function for particle swarm optimization
def particleSwarmOptimization(costFunction, x0, bounds, num_particles, maxiter):
    # Initialize the swarm
    global numStartingLocation
    numStartingLocation = len(x0)
    print(numStartingLocation)
    bestGroupError = -1
    groupsBestPosition = []
    swarm = []

    #Initialize the
    for i in range(0, num_particles):
        swarm.append(individualParticle(x0))

    # loop to start the optimization process
    for i in range(0, maxiter):
        # Evaluate each agent's fitness
        for j in range(0, num_particles):
            swarm[j].evaluate(costFunction)

            # Which agent has the best position (minimum error) in the swarm?
            if swarm[j].individualError < bestGroupError or bestGroupError == -1:
                groupsBestPosition = list(swarm[j].individualPosition)
                bestGroupError = float(swarm[j].individualError)

        for j in range(0, num_particles):
            swarm[j].update_velocity(groupsBestPosition)
            swarm[j].positionUpdate(bounds)

    print('After running the swarm of computer agents, the group\'s best position is '+
          str(groupsBestPosition) + " with an error of " + str(bestGroupError))

# Initialize the starting position for every particle in each dimension (dimension=2), and boundaries for search
initialStartingPosition = [-15, 15]
minMaxBounds = [(-100,100), (-100,100)]

particleSwarmOptimization(errorFunction, initialStartingPosition, minMaxBounds,
                          num_particles = 150, maxiter = 30)

'''

EXERCISE 3
g(x) = 50sin(x) + x^2 + 100
The particle has trouble finding the global minimum at low velocity because of the chosen inertia weight, w
The inertia weight is responsible for controlling the direction of the 'explosion' of the PSO trajectory

    cognitiveVelocity = c1 * r1 * (self.individualBestPosition[i] - self.individualPosition[i])
    socialVelocity = c2 * r2 * (groupsBestPosition[i] - self.individualPosition[i])
    self.individualVelocity[i] = w * self.individualVelocity[i] + cognitiveVelocity + socialVelocity


The inertia weight continues to reduce the previous velocity by a significant amount for each iteration (50 percent)
With such tiny changes in the position of a particle from its previous position, it finds it hard to 
move on from the local minimum. 
Changing the weight to 1.0 allows the velocity to grow

'''

















