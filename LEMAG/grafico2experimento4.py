import numpy as np
import matplotlib.pyplot as plt

MU0 = 4 * np.pi * 1e-7
I = 1.0
d_mm = 40


def calcular_B(N, L_mm, d_mm, z_cm):
    l = L_mm / 1000.0
    a = (d_mm / 2.0) / 1000.0
    z = z_cm / 100.0

    termo1 = (l / 2 - z) / np.sqrt(a**2 + (l / 2 - z)**2)
    termo2 = (l / 2 + z) / np.sqrt(a**2 + (l / 2 + z)**2)

    B_tesla = ((MU0 * N * I) / (2 * l)) * (termo1 + termo2)
    return B_tesla * 1000


distancia = np.arange(0, 18, 1)

tab3_N1_medido = [
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
]
tab3_N2_medido = [
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
]
tab3_N3_medido = [
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

eixoz = np.linspace(0, 17, 200)

plt.figure(figsize=(10, 6))

plt.scatter(
    distancia, tab3_N1_medido, color="blue", label="Exp (N=100, L=53mm)"
)
plt.scatter(
    distancia, tab3_N2_medido, color="green", label="Exp (N=200, L=105mm)"
)
plt.scatter(
    distancia, tab3_N3_medido, color="red", label="Exp (N=300, L=160mm)"
)

plt.plot(
    eixoz,
    calcular_B(100, 53, d_mm, eixoz),
    "--",
    color="blue",
    label="Teo (N=100, L=53mm)",
)
plt.plot(
    eixoz,
    calcular_B(200, 105, d_mm, eixoz),
    "--",
    color="green",
    label="Teo (N=200, L=105mm)",
)
plt.plot(
    eixoz,
    calcular_B(300, 160, d_mm, eixoz),
    "--",
    color="red",
    label="Teo (N=300, L=160mm)",
)

plt.title(
    "Densidade de fluxo magnético ao longo do eixo dos solenoides (d fixo)"
)
plt.xlabel("Posição z (cm)")
plt.ylabel("Densidade de Fluxo B (mT)")
plt.grid(True, which="both", linestyle=":", alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()
