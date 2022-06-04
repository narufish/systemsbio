import PyQt5
import numpy as np
import matplotlib
#matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#qt5 backend
#size of the grid (universe)
universe = 50
alive = 1 # alive cells = "on"
dead = 0 # dead cells = "off"
#list of values "on" and "off" used to populate the initial universe
vals = [alive,dead]

#populate the universe with random cells
grid = np.random.choice(vals, universe*universe, p=[0.1,0.9]).reshape(universe,universe)

# define a function to animate the cells in the universe
# animated_universe is a void function, but placeholder values *arg, *kwards necessary for matplotlib initial value (framerate)
def animated_universe(framenumber, *arg, **kwargs):
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
            if grid[i,j] == alive:
                if (total<2) or (total>3):
                    newGrid[i,j] = dead
            else:
                if total == 3:
                    newGrid[i,j] = alive

    grid = newGrid.copy()
    mat.set_data(grid)
    return mat

fig, ax = plt.subplots()
mat = ax.matshow(grid)
# interval : number, optional
# Delay between frames in milliseconds. Defaults to 200.
# save_count : int, optional
# The number of values from frames to cache.

ani = animation.FuncAnimation(fig, animated_universe, interval=3)
# use higher interval to observe oscillator
# ani = animation.FuncAnimation(fig, animated_universe, interval=60)
plt.show()
ani.save('animation.gif', writer='imagemagick', fps=30)

#            if (beehive == grid[i:(i + 3) % universe, j:(j + 2) % universe]).all():
#               print("The 'aforall' oscillator is detected.")















