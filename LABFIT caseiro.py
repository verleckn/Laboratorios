import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

E = 2.5 * 10**3  # V/m


def calcular_V(E, x_cm):
    x = x_cm * 10**-2  # m
    V = E * x
    return V  # V


def modelo(x, a, b, c):
    y = a * x**2 + b * x + c
    return y


distancia = np.arange(0, 12, 2)  # cm

V_med25 = np.array([14.0, 21.0, 37.5, 55.0, 103.0, 125.0])  # V
V_med40 = np.array([12.5, 21.0, 22.0, 47.0, 66.5, 70.0])  # V

popt25, _ = curve_fit(modelo, distancia, V_med25)
popt40, _ = curve_fit(modelo, distancia, V_med40)

eixo_x = np.linspace(0, 10, 100)  # cm

plt.figure(figsize=(10, 6))

plt.scatter(distancia, V_med25, color="blue", label="Exp: L = 2,5 cm")
plt.scatter(distancia, V_med40, color="red", label="Exp: L = 4,0 cm")

plt.plot(
    eixo_x,
    calcular_V(E, eixo_x),
    color="gold",
    label="Teo: Centro Placas",
)
plt.plot(
    eixo_x,
    modelo(eixo_x, *popt25),
    "--",
    color="blue",
    label="Ajuste L = 2,5 cm",
)
plt.plot(
    eixo_x,
    modelo(eixo_x, *popt40),
    "--",
    color="red",
    label="Ajuste L = 4,0 cm",
)

plt.xlabel("Distância da Sonda (cm)")
plt.ylabel("Potencial Elétrico (V)")
plt.grid(True, which="both", linestyle=":", alpha=0.6)

plt.xlim(0, 10)
plt.ylim(0, 250)

plt.legend()
plt.tight_layout()
plt.show()
