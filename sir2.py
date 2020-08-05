import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate, optimize

coronavirus_data = pd.read_excel('coronavirus.xlsx', sheet_name='全国')

ydata = list(coronavirus_data['Infections'].dropna())
xdata = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
days = coronavirus_data['Date'].dt.strftime('%b %d')

ydata = np.array(ydata, dtype=float)
xdata = np.array(xdata, dtype=float)

def sir_model(y, x, beta, gamma):
    S = -beta * y[0] * y[1] / N
    R = gamma * y[1]
    I = -(S + R)
    return S, I, R

def fit_odeint(x, beta, gamma):
    return integrate.odeint(sir_model, (S0, I0, R0), x, args=(beta, gamma))[:,1]

# initial conditions
N = 80000
I0 = ydata[0]
S0 = N - I0
R0 = 0.0

popt, pcov = optimize.curve_fit(fit_odeint, xdata, ydata)
fitted = fit_odeint(xdata, *popt)

fig = plt.figure(figsize=(12, 8), dpi=150)
plt.plot(days, fitted, color=(1.0, 0.2471, 0.2471))
plt.plot(days, ydata, color='dodgerblue', marker='.', linestyle="")
plt.legend(["S(t)", "NHC Data"])
plt.xticks(rotation=90)
#plt.xticks(sol.t," ")
#plt.yticks(sol.t," ")
plt.show()


print(popt)
print(popt[0]/popt[1])
print(pcov)
print(pcov[0][0]**(0.5))
print(pcov[1][1]**(0.5))
print(1/popt[1])
