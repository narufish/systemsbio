import numpy as np
from scipy.stats import logistic
import matplotlib.pyplot as plt

def sigmoid(x):
    y = 1/(1 + np.exp(-x))
    return y

def reLU(x):
    y = max(0,x)
    return y

def tanh(x):
    y = (np.exp(x)-np.exp(-x))/(np.exp(-x)+np.exp(x))
    return y

x = np.linspace(-10, 10, 100) #array of x value from -10 to 10 at 100 increments
#y = sigmoid(x)
y = [reLU(i) for i in x]
#y = [tanh(i) for i in x]
print(np.exp(1))
print(np.exp(-1))
print(tanh(1))
'''
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.show()
'''
#logistic.cdf(x)