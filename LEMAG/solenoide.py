import numpy as np

MU0 = 4 * np.pi * 10**-7  # H/m
I = 1.0  # A


def calcular_B(N, L_mm, d_mm, z_cm):
    l = L_mm * 10**-3  # m
    a = d_mm * 10**-3 / 2  # m
    z = z_cm * 10**-2  # m

    termo1 = (l / 2 - z) / np.sqrt(a**2 + (l / 2 - z) ** 2)
    termo2 = (l / 2 + z) / np.sqrt(a**2 + (l / 2 + z) ** 2)

    B_tesla = ((MU0 * N * I) / (2 * l)) * (termo1 + termo2)  # T
    return B_tesla * 1000  # mT
