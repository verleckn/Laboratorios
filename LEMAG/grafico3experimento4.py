import numpy as np
import matplotlib.pyplot as plt

from solenoide import calcular_B

N = 300  # adimensional
L_mm = 160  # mm


distancia = np.arange(0, 18, 1)  # cm

tab4_sol1_medido = [
    2.33,
    2.33,
    2.31,
    2.30,
    2.28,
    2.25,
    2.21,
    2.06,
    1.67,
    0.82,
    0.29,
    0.13,
    0.08,
    0.04,
    0.03,
    0.03,
    0.03,
    0.02,
]  # mT, onde N = 300, L = 160 mm, d = 25 mm
tab4_sol2_medido = [
    2.27,
    2.25,
    2.20,
    2.17,
    2.15,
    2.10,
    1.96,
    1.76,
    1.40,
    0.88,
    0.44,
    0.24,
    0.15,
    0.08,
    0.05,
    0.04,
    0.03,
    0.00,
]  # mT, onde N = 300, L = 160 mm, d = 40 mm
tab4_sol3_medido = [
    2.27,
    2.24,
    2.22,
    2.21,
    2.20,
    2.19,
    2.10,
    1.95,
    1.55,
    0.80,
    0.40,
    0.20,
    0.10,
    0.07,
    0.05,
    0.04,
    0.02,
    0.01,
]  # mT, onde N = 300, L = 160 mm, d = 32 mm

eixoz = np.linspace(0, 17, 200)  # cm

plt.figure(figsize=(10, 6))

plt.scatter(distancia, tab4_sol1_medido, color="blue", label="Exp (d = 25 mm)")
plt.scatter(
    distancia, tab4_sol2_medido, color="green", label="Exp (d = 40 mm)"
)
plt.scatter(distancia, tab4_sol3_medido, color="red", label="Exp (d = 32 mm)")

plt.plot(
    eixoz,
    calcular_B(N, L_mm, 25, eixoz),
    "--",
    color="blue",
    label="Teo (d = 25 mm)",
)
plt.plot(
    eixoz,
    calcular_B(N, L_mm, 40, eixoz),
    "--",
    color="green",
    label="Teo (d = 40 mm)",
)
plt.plot(
    eixoz,
    calcular_B(N, L_mm, 32, eixoz),
    "--",
    color="red",
    label="Teo (d = 32 mm)",
)

plt.title(
    "Densidade de fluxo magnético ao longo do eixo dos solenoides (N fixo)"
)
plt.xlabel("Posição z (cm)")
plt.ylabel("Densidade de Fluxo B (mT)")
plt.grid(True, which="both", linestyle=":", alpha=0.7)

plt.xlim(0, 17)
plt.ylim(0, 2.5)

plt.legend()
plt.tight_layout()
plt.show()
