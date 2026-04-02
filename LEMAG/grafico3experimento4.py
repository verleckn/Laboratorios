import numpy as np
import matplotlib.pyplot as plt

MU0 = 4 * np.pi * 1e-7
I = 1.0
N = 300
L_mm = 160


def calcular_B(N, L_mm, d_mm, z_cm):
    l = L_mm / 1000.0
    a = (d_mm / 2.0) / 1000.0
    z = z_cm / 100.0

    termo1 = (l / 2 - z) / np.sqrt(a**2 + (l / 2 - z)**2)
    termo2 = (l / 2 + z) / np.sqrt(a**2 + (l / 2 + z)**2)

    B_tesla = ((MU0 * N * I) / (2 * l)) * (termo1 + termo2)
    return B_tesla * 1000


distancia = np.arange(0, 18, 1)

tab4_N1_medido = [
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
]
tab4_N2_medido = [
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
]
tab4_N3_medido = [
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
]

eixoz = np.linspace(0, 17, 200)

plt.figure(figsize=(10, 6))

plt.scatter(distancia, tab4_N1_medido, color="blue", label="Exp (d=25mm)")
plt.scatter(distancia, tab4_N2_medido, color="green", label="Exp (d=32mm)")
plt.scatter(distancia, tab4_N3_medido, color="red", label="Exp (d=40mm)")

plt.plot(
    eixoz,
    calcular_B(N, L_mm, 25, eixoz),
    "--",
    color="blue",
    label="Teo (d=25mm)",
)
plt.plot(
    eixoz,
    calcular_B(N, L_mm, 32, eixoz),
    "--",
    color="green",
    label="Teo (d=32mm)",
)
plt.plot(
    eixoz,
    calcular_B(N, L_mm, 40, eixoz),
    "--",
    color="red",
    label="Teo (d=40mm)",
)

plt.title(
    "Densidade de fluxo magnético ao longo do eixo dos solenoides (N fixo)"
)
plt.xlabel("Posição z (cm)")
plt.ylabel("Densidade de Fluxo B (mT)")
plt.grid(True, which="both", linestyle=":", alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()
