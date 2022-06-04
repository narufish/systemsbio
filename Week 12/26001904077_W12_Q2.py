import matplotlib.pyplot as plt
import numpy as np

# Displays the options for which function to visualize
print("Functions:")
print("[1] f(x) = 5*(x-20)^2")
print("[2] g(x) = 50*sin(x) + x^2 + 100")
print("[3] h(x) = 15*sin((x/2)^2) * 75*cos(x/13) * 3*sin(x/6) + x^2 + 300")

# program asks for valid integer input (1,2,3) from the user
while True:
    choice = input("Choose which function to visualize [1,2,3]:")
    try:#if the user entered a non-integer or integer which are not in the range 1<= x <=3, then user is asked to input again
        choice = int(choice)
        if choice>=1 and choice<=3:
            break
        else:
            print("Please enter valid integer input")
    except ValueError:
        print("Please enter integer input")

# functions f(x), g(x), h(x) in equation 1,2 and 3
def f(x):
    y = 5*(x-20)**2
    return y

def g(x):
    y = 50*np.sin(x) + x**2 + 100
    return y

def h(x):
    y = 15*np.sin((x/2)**2) * 75*np.cos(x/13) * 3*np.sin(x/6) + x**2 + 300
    return y

# the range for the x axis is from -100 to 100
x = np.linspace(-100,100,100)

# determines which function to display based on user input(choice)
if choice==1:
    y = f(x)
elif choice==2:
    y = g(x)
elif choice==3:
    y = h(x)

# plots the graph and displays it
plt.plot(x,y)
plt.show()