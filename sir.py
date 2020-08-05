import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

N = 1000
beta, gamma = [0.5, 0.1]

def SIR(t,y):
    S = y[0]
    I = y[1]
    R = y[2]
    return([-beta*S*I*(1/N), beta*S*I*(1/N)-gamma*I, gamma*I])

sol = solve_ivp(SIR, [0, 112], [N, 1, 0], t_eval=np.arange(0, 112.2, 0.2))

fig = plt.figure(figsize=(12, 8), dpi=150)
plt.plot(sol.t, sol.y[0], color=(0.9725, 0.9490, 0.0))
plt.plot(sol.t, sol.y[1], color=(1.0, 0.2471, 0.2471))
plt.plot(sol.t, sol.y[2], color=(0.0, 0.6902, 0.3137))
plt.xlabel('Day')
plt.legend(["S(t)", "I(t)", "R(t)"])
plt.show()