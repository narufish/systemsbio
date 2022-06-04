import numpy as np
import matplotlib.pyplot as plt

#making the grid for the visualization
universe = np.zeros((12,12))
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

# setting the position of the pattern in the grid
universe[1:11, 1:11] = aforall

plt.imshow(universe,cmap='binary')
plt.show()
