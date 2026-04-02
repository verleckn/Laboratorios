import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

E = 2.5 * 10**3  # V / m

d = np.array([0, 2, 4, 6, 8, 10])  # cm
v_med25 = np.array([14.0, 21.0, 37.5, 55.0, 103.0, 125.0])  # V
v_med40 = np.array([12.5, 21.0, 22.0, 47.0, 66.5, 70.0])  # V


def calcula_v_teoc(d, E):
    v_teoc = E * d * 10**-2
    return v_teoc  # V


def modelo(x, a, b, c):
    y = a * x**2 + b * x + c
    return y


popt25, _ = curve_fit(modelo, d, v_med25)
popt40, _ = curve_fit(modelo, d, v_med40)

eixo_x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))

plt.plot(
    eixo_x,
    calcula_v_teoc(eixo_x, E),
    color="yellow",
    label="Teo: Centro Placas",
)

plt.scatter(d, v_med25, color="blue", label="Exp: L = 2,5 cm")
plt.plot(
    eixo_x,
    modelo(eixo_x, *popt25),
    "--",
    color="blue",
    label="Ajuste L = 2,5 cm",
)

plt.scatter(d, v_med40, color="red", label="Exp: L = 4,0 cm")
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
plt.legend()
plt.tight_layout()

plt.show()
