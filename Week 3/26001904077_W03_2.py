
import matplotlib.pyplot as plt
import numpy as np

# display parameter changes the region of the mandelbrot set to be displayed
def showMandelbrot_set(line_res, iter_num, display):
    #changes the display to full mandelbrot set, elephant valley, or seahorse valley depending on input in display parameter
    if(display==0): # full mandelbrot set
        left_bound = -2.0
        right_bound =  0.5
        upper_bound = 1.0
        lower_bound = -1.0

    # seahorse valley is centered around -0.75 + 0.1i
    elif(display==1):
        left_bound = -0.85
        right_bound = -0.65
        upper_bound = 0.20
        lower_bound = 0.0

    # elephant valley is centered around 0.3 + 0i, size of 0.1 + 0.1i
    elif(display==2):
        left_bound = 0.2
        right_bound = 0.4
        upper_bound = 0.1
        lower_bound = -0.1

    x_val = np.linspace(left_bound, right_bound, line_res)  # this defines the left and right boundaries to the function
    y_val = np.linspace(lower_bound, upper_bound, line_res)  # defines the upper and lower boundaries to the function
    M = np.zeros([line_res, line_res], int)

    for u, x in enumerate(x_val):
        for v, y in enumerate(y_val):
            z = 0 + 0j;  # intialization is set to 0
            # Range is translated to a complex number, it is visualized in 2 dimensions (real part is plotted against the imaginary part)
            # coordinates of (-1,0.5) becomes -1 + 05j
            c = complex(x, y);#this value will be used as input for the recurrent function

            #The recurrence occurs for the number of iterations fixed in the functions parameters
            for i in range(iter_num):
                z = z * z + c # quadratic recurrence equation that produces the set
                # For example, a value of -1 + 0j, yields the following output -> -1, 0, -1, 0, ...
                # the does not approach infinity and is stable, thus, it is included in the set
                # On the other hand, if we plugged 1 + 0j into the function, it yields -> 1, 2, 5, 26, ...
                # the z value approaches infinity and is not stable, thus, it is not included in the set

                # this checks to see if the z value eventually blows up into infinity or not
                # if the cummulative absolute value of the z goes into infinity, it is not included in the set
                # z it is included in the set, if the final accumulative value becomes less then 2.0
                if abs(z) > 2.0:
                    M[v, u] = 1 #the value of 1 is displayed as white in the plot
                    break

    plt.imshow(M, origin="lower", extent=(left_bound, right_bound, lower_bound, upper_bound))  # creating the image with axes label
    plt.gray()  # grayscale image
    plt.show()  # image output


showMandelbrot_set(1000, 100, 2)

