import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Total population: N
N = 10000
# Number of infected at time t=0
I0 = 1
# Number of removed (either die to immunity or by death) at time t=0
R0 = 0
#All susceptible individuals at time t=0
S0 = N - I0 - R0

#Contact rate (how infectious a contagion spreads)
beta = 0.7
#Infectious period (inverse of the number of days) or recovery time, how long the individual stays in the infectious compartment
gamma = float(1/7)#3
# Time from day 0 to day 100 in 1-hour increments
t = np.linspace(0, 100, num=2400)

def SIRmodel(compartmentValues, t, N, beta, gamma):
    S, I, R = compartmentValues
    dSdt = -beta * S * I/N
    dIdt = beta * S * I/N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Vector with initial conditions
compartmentValues0 = S0, I0, R0

# Integrate the SIR equations over the time grid t
# and return numerical solutions
SIRmodelNumSolve = odeint(SIRmodel, compartmentValues0, t, args=(N, beta, gamma))
S, I, R = SIRmodelNumSolve.T

# White background
fig = plt.figure(facecolor='w')
# 1x1 grid with one plot, light gray background
ax = fig.add_subplot(1,1,1, facecolor='#eeeeee', axisbelow=True)
#Plot the data for three seperate curves: S(t), I(t) and R(t)
ax.plot(t, S/N, "b", alpha=0.2, lw=1, label="Susceptible")
ax.plot(t, I/N, "r",  lw=2, label="Infected")
ax.plot(t, R/N, "g", alpha=0.2, lw=1, label="Removed")
# Axis labeling
ax.set_xlabel("Time in days")
ax.set_ylabel("Individuals (in " + str(N) + "s)")
# Call matplotlib function to print the graph legend
ax.legend()
# The moment of truth
plt.show()




























