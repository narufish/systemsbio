
import matplotlib.pyplot as plt
import numpy as np

#parameters are line resoultion, number of iterations, left boundary, right boundary, upper boundary, lower boundary
def showMandelbrot_set(line_res, iter_num, left_bound,right_bound,upper_bound,lower_bound):
    x_val = np.linspace(left_bound, right_bound, line_res)  # this defines the left and right boundaries to the function
    y_val = np.linspace(lower_bound, upper_bound, line_res)  # defines the upper and lower boundaries to the function
    M = np.zeros([line_res, line_res], int)

    for u, x in enumerate(x_val):
        for v, y in enumerate(y_val):
            z = 0 + 0j;  # intialization is set to 0
            # transforms the range to a complex number
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

    plt.imshow(M, origin="lower",
               extent=(left_bound, right_bound, lower_bound, upper_bound))  # creating the image with axes label
    plt.gray()  # grayscale image
    plt.show()  # image output


showMandelbrot_set(1000, 50, -2, 0.5, 1, -1)







