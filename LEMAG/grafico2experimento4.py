import numpy as np
import matplotlib.pyplot as plt

from solenoide import calcular_B

d_mm = 40  # mm

distancia = np.arange(0, 18, 1)  # cm

tab3_sol1_medido = [
    1.83,
    1.74,
    1.45,
    0.90,
    0.49,
    0.22,
    0.10,
    0.05,
    0.04,
    0.01,
    0.01,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
    0.00,
]  # mT, onde N = 100, L = 53 mm, d = 40 mm
tab3_sol2_medido = [
    2.17,
    2.17,
    2.15,
    2.09,
    2.00,
    1.65,
    1.20,
    0.64,
    0.33,
    0.27,
    0.15,
    0.12,
    0.10,
    0.08,
    0.08,
    0.07,
    0.07,
    0.06,
]  # mT, onde N = 200, L = 105 mm, d = 40 mm
tab3_sol3_medido = [
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

eixoz = np.linspace(0, 17, 200)  # cm

plt.figure(figsize=(10, 6))

plt.scatter(
    distancia, tab3_sol1_medido, color="blue", label="Exp (N = 100, L = 53 mm)"
)
plt.scatter(
    distancia,
    tab3_sol2_medido,
    color="green",
    label="Exp (N = 200, L = 105 mm)",
)
plt.scatter(
    distancia, tab3_sol3_medido, color="red", label="Exp (N = 300, L = 160 mm)"
)

plt.plot(
    eixoz,
    calcular_B(100, 53, d_mm, eixoz),
    "--",
    color="blue",
    label="Teo (N = 100, L = 53 mm)",
)
plt.plot(
    eixoz,
    calcular_B(200, 105, d_mm, eixoz),
    "--",
    color="green",
    label="Teo (N = 200, L = 105 mm)",
)
plt.plot(
    eixoz,
    calcular_B(300, 160, d_mm, eixoz),
    "--",
    color="red",
    label="Teo (N = 300, L = 160 mm)",
)

plt.title(
    "Densidade de fluxo magnético ao longo do eixo dos solenoides (d fixo)"
)
plt.xlabel("Posição z (cm)")
plt.ylabel("Densidade de Fluxo B (mT)")
plt.grid(True, which="both", linestyle=":", alpha=0.7)

plt.xlim(0, 17)
plt.ylim(0, 2.5)

plt.legend()
plt.tight_layout()
plt.show()
