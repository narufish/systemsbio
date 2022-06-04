"""
Created on 9/11/2021

@author: Alina Hazirah Ramlan
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#size of the grid (universe)
universe = 50
alive = 1 # alive cells = "on"
dead = 0 # dead cells = "off"
#list of values "on" and "off" used to populate the initial universe
vals = [alive,dead]

#initilize skew values for random grid population
alive_cells = 0.1
dead_cells = 0.9

# asks the user to enter which cellular automaton to simulate (1:maze, 2:move)
choice = int(input("Select which cellular automaton to simulate (1:maze, 2:move): "))

#checks whether user has entered valid input
# also sets the appropriate skew values in the random grid initialization to properly visualize the cellular automaton
while choice:
    if choice==1:
        alive_cells = 0.05
        dead_cells = 0.95
        break
    elif choice==2:
        alive_cells = 0.6
        dead_cells = 0.4
        break
    else: #asks the user ti input valid input if invalild input is entered
        choice = int(input("Please enter valid input (1:maze, 2:move):"))

#populate the universe with random cells
grid = np.random.choice(vals, universe*universe, p=[alive_cells,dead_cells]).reshape(universe,universe)

# function to animate the maze cellular automaton
# animated_universe is a void function, but placeholder values *arg, *kwards necessary for matplotlib initial value (framerate)
def animated_universe_maze(framenumber, *arg, **kwargs):
    global grid
    global animatedcount
    newGrid = grid.copy()
    for i in range(universe):
        for j in range(universe):
            total = (grid[i, (j-1)%universe]+
                     grid[i, (j+1)%universe]+
                     grid[(i-1)%universe,j]+ grid[(i+1)%universe, j]+
                     grid[(i-1)%universe,(j-1)%universe]+ grid[(i-1)%universe,(j+1)%universe]+
                     grid[(i+1)%universe,(j-1)%universe]+ grid[(i+1)%universe,(j+1)%universe])/alive
                    #rules for a cell dying off or staying alive
            if grid[i,j] == alive:#cell stays alive if  there are 1,2,3,4 or 5 neighbour cells
                if (total==0) or (total>5):# otherwise the cell dies
                    newGrid[i,j] = dead
            else:# if the total number of neighbour cells is three in dead state, the cell comes alive
                if total == 3:
                    newGrid[i,j] = alive
    grid = newGrid.copy()
    mat.set_data(grid)
    return mat

# function to animate the move cellular automaton
def animated_universe_move(framenumber, *arg, **kwargs):
    global grid
    global animatedcount
    newGrid = grid.copy()
    for i in range(universe):
        for j in range(universe):
            total = (grid[i, (j - 1) % universe] +
                grid[i, (j + 1) % universe] +
                grid[(i - 1) % universe, j] + grid[(i + 1) % universe, j] +
                grid[(i - 1) % universe, (j - 1) % universe] + grid[(i - 1) % universe, (j + 1) % universe] +
                grid[(i + 1) % universe, (j - 1) % universe] + grid[
                (i + 1) % universe, (j + 1) % universe]) / alive
            # rules for a cell dying off or staying alive
            if grid[i, j] == alive:# cell stays alive if there are 2,4 or 5 neighbour cells
                if (total == 3) or (total < 2) or (total>5):# otherwise the cell dies off
                    newGrid[i, j] = dead
            else: #a dead cell comes alive if there are 3,6, or 8 neighbour cells
                if (total == 3) or (total == 6) or (total == 8):
                    newGrid[i, j] = alive

    grid = newGrid.copy()
    mat.set_data(grid)
    return mat

fig, ax = plt.subplots()
mat = ax.matshow(grid)

# changes the universe to be animated according to user input
if choice==1:
    animated_universe = animated_universe_maze

elif choice==2:
    animated_universe = animated_universe_move

# interval set to 200 to properly see the animation of the cellular automaton
ani = animation.FuncAnimation(fig, animated_universe, interval=200)
plt.show()
















