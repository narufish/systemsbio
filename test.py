import numpy as np
import matplotlib.pyplot as plt
'''
#calculates the mean of a fixed length (random numbers)
def random_n(length):
    n=0
    x = np.random.randint(0,10,length)
    #plt.plot([length/11 for i in range(10)])
    for j in x:
        n += j
    m = n/length
    return m

# plots the array of mean of the length of numbers from random_n
def meanval_rand(length,rand_n):
    val = [random_n(rand_n) for i in range(length)]
    plt.hist(val)
    plt.show()

np.random.seed(10)
meanval_rand(100,100)

print(np.true_divide(1,0))
'''
'''
target = "Alina Hazirah"
competingDNA = "alinaydavhjaa"

fitness = 0
for i in range(len(competingDNA)):
    if competingDNA[i] != target[i]:
        fitness += 1

print(fitness)

print(ord('b'))
'''''
plt.subplot(2,2,1)
plt.plot([1,2,3,4])

plt.subplot(2,2,2)
plt.plot([1,2,3,4])

plt.subplot(2,2,3)
plt.plot([1,2,3,4])

plt.subplot(2,2,4)
plt.plot([1,2,3,4])

plt.show()

'''
    def update_velocity(self, groupsBestPosition,iter,maxiter,r1,r2):
        w_bounds = [0.1,0.5]
        #w = 0.5     # Inertia weight of previous velocity
        c1 = 1      # Cognitive constant (distance from the individual's known best position)
        c2 = 2      # Social constant (distance from the group's known best position)
        w = w_bounds[1] - (w_bounds[1]-w_bounds[0]) * (iter/maxiter)

        # Random numbers to compensate for the cognitive and social constants
        for i in range(0, numStartingLocation):
            r1 = 4 * r1 * (1-r1)
            r2 = 4 * r2 * (1-r2)
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

def particleSwarmOptimization(costFunction, x0, bounds, num_particles, maxiter):
    # Initialize the swarm
    global numStartingLocation
    numStartingLocation = len(x0)
    print(numStartingLocation)
    bestGroupError = -1
    groupsBestPosition = []
    swarm = []
    r1 = 1
    r2 = 1

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
            swarm[j].update_velocity(groupsBestPosition,i,maxiter,r1,r2)
            swarm[j].positionUpdate(bounds)

    print('After running the swarm of computer agents, the group\'s best position is '+
          str(groupsBestPosition) + " with an error of " + str(bestGroupError))

initialStartingPosition = [-15, 15]
minMaxBounds = [(-100,100), (-100,100)]
particleSwarmOptimization(errorFunction, initialStartingPosition, minMaxBounds,
                          num_particles = 150, maxiter = 1000)
'''