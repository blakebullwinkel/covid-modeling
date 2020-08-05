import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

N = 2444
beta, gamma, epsilon = [0.528, 0.146, 0.382]

def SIQR(t,y):
    S = -beta*y[0]*y[1] / N
    R = (gamma*y[1]) + (gamma*y[2])
    Q = (epsilon*y[1]) - (gamma*y[2])
    I = -(S + R + Q)
    return S, I, Q, R

sol = solve_ivp(SIQR, [0, 112], [N, 1, 0, 0], t_eval=np.arange(0, 112.2, 0.2))

fig = plt.figure(figsize=(12, 8), dpi=150)
plt.plot(sol.t, sol.y[0], color=(0.9725, 0.9490, 0.0))
plt.plot(sol.t, sol.y[1], color=(1.0, 0.2471, 0.2471))
plt.plot(sol.t, sol.y[2], color=(1.0, 0.6, 0.0))
plt.plot(sol.t, sol.y[3], color=(0.0, 0.6902, 0.3137))
plt.xlabel('Day')
plt.legend(["S(t)", "I(t)", "Q(t)", "R(t)"])
plt.show()