
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#size of the grid (universe)
universe = 12
# there are only two states in the game
alive = 1 # alive cells = "on"
dead = 0 # dead cells = "off"

#list of values "on" and "off" used to populate the initial universe
vals = [alive,dead]
#the oscillator visualized is called "aforall"

aforall = [[0,0,0,0,1,1,0,0,0,0],
        [0,0,0,1,0,0,1,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,1,0,1,0,0,1,0,1,0],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [0,1,0,1,0,0,1,0,1,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,1,0,0,1,0,0,0],
        [0,0,0,0,1,1,0,0,0,0]]


# create the grid for the oscillator
grid = np.zeros((universe,universe))
# set the position of the oscillator in the grid
grid[1:11, 1:11] = aforall

# define a function to animate the cells in the universe
# animated_universe is a void function, but placeholder values *arg, *kwards necessary for matplotlib initial value (framerate)
def animated_universe(framenumber, *arg, **kwargs):
    global grid
    global animatedcount
    newGrid = grid.copy()
    # the algorithm iterates through the grid and checks the number of alive squares surrounding a block
    for i in range(universe):
        for j in range(universe):
            total = (grid[i, (j-1)%universe]+
                     grid[i, (j+1)%universe]+
                     grid[(i-1)%universe,j]+ grid[(i+1)%universe, j]+
                     grid[(i-1)%universe,(j-1)%universe]+ grid[(i-1)%universe,(j+1)%universe]+
                     grid[(i+1)%universe,(j-1)%universe]+ grid[(i+1)%universe,(j+1)%universe])/alive
                    #rules for a cell dying off or staying alive
            # an alive block becomes dead if there are less than 2 or more than 3 alive blocks surrounding it
            if grid[i,j] == alive:
                if (total<2) or (total>3):
                    newGrid[i,j] = dead
            # otherwise, if there are exactly 3 alive blocks surrounding the block, it comes back to life
            else:
                if total == 3:
                    newGrid[i,j] = alive
    # updates the grid with the new alive and dead blocks
    grid = newGrid.copy()
    mat.set_data(grid)
    return mat

# create a figure and one subplot
fig, ax = plt.subplots()
# displays the grid as a figure
mat = ax.matshow(grid)

# interval set to 150 to properly view the changes that occur in the animation
ani = animation.FuncAnimation(fig, animated_universe, interval=500)

plt.show()
#ani.save('animation.gif', writer='imagemagick', fps=30)

















