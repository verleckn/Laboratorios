import numpy as np
import matplotlib.pyplot as plt

MU0 = 4 * np.pi * 1e-7
I = 1.0
L_mm = 160
d_mm = 25


def calcular_B(N, L_mm, d_mm, z_cm):
    l = L_mm / 1000.0
    a = (d_mm / 2.0) / 1000.0
    z = z_cm / 100.0

    termo1 = (l / 2 - z) / np.sqrt(a**2 + (l / 2 - z)**2)
    termo2 = (l / 2 + z) / np.sqrt(a**2 + (l / 2 + z)**2)

    B_tesla = ((MU0 * N * I) / (2 * l)) * (termo1 + termo2)
    return B_tesla * 1000


distancia = np.arange(0, 18, 1)

tab2_N1_medido = [
    0.54,
    0.54,
    0.54,
    0.54,
    0.53,
    0.53,
    0.52,
    0.50,
    0.49,
    0.38,
    0.20,
    0.09,
    0.05,
    0.03,
    0.03,
    0.02,
    0.02,
    0.01,
]
tab2_N2_medido = [
    1.20,
    1.21,
    1.22,
    1.21,
    1.20,
    1.20,
    1.18,
    1.12,
    0.99,
    0.57,
    0.24,
    0.11,
    0.06,
    0.04,
    0.04,
    0.04,
    0.03,
    0.03,
]
tab2_N3_medido = [
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

eixoz = np.linspace(0, 17, 200)

plt.figure(figsize=(10, 6))

plt.scatter(distancia, tab2_N1_medido, color="blue", label="Exp (N=75)")
plt.scatter(distancia, tab2_N2_medido, color="green", label="Exp (N=150)")
plt.scatter(distancia, tab2_N3_medido, color="red", label="Exp (N=300)")

plt.plot(
    eixoz,
    calcular_B(75, L_mm, d_mm, eixoz),
    "--",
    color="blue",
    label="Teo (N=75)",
)
plt.plot(
    eixoz,
    calcular_B(150, L_mm, d_mm, eixoz),
    "--",
    color="green",
    label="Teo (N=150)",
)
plt.plot(
    eixoz,
    calcular_B(300, L_mm, d_mm, eixoz),
    "--",
    color="red",
    label="Teo (N=300)",
)

plt.title(
    "Densidade de fluxo magnético ao longo do eixo dos solenoides (d e L fixos)"
)
plt.xlabel("Posição z (cm)")
plt.ylabel("Densidade de Fluxo B (mT)")
plt.grid(True, which="both", linestyle=":", alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()
