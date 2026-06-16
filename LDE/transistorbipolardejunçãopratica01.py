import matplotlib.pyplot as plt
import numpy as np

VB = np.array(
    [
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.64,
        0.63,
        0.62,
        0.61,
        0.6,
        0.6,
    ]
)  # V

VCE = np.array(
    [
        5.00,
        4.25,
        3.93,
        3.52,
        3.32,
        3.03,
        2.5,
        2.12,
        1.96,
        1.44,
        0.95,
        0.59,
        0.26,
        0.23,
        0.17,
        0.14,
        0.1,
        92.3e-3,
        77.5e-3,
        66.1e-3,
        56.9e-3,
    ]
)  # V

IC = (
    np.array(
        [
            2.99e-3,
            2.98e-3,
            2.97e-3,
            2.96e-3,
            2.95e-3,
            2.94e-3,
            2.92e-3,
            2.91e-3,
            2.9e-3,
            2.88e-3,
            2.85e-3,
            2.81e-3,
            2.55e-3,
            2.44e-3,
            2.13e-3,
            1.66e-3,
            0.99e-3,
            0.77e-3,
            0.5e-3,
            0.34e-3,
            0.24e-3,
        ]
    )
    * 1000
)  # mA


plt.figure(figsize=(9, 6))
plt.scatter(VCE, IC)
plt.plot(VCE, IC, "--")
plt.xlabel("$V_{CE}$ (V)")
plt.ylabel("$I_{C}$ (mA)")

plt.grid(True, which="both", linestyle=":", alpha=0.6)
plt.tight_layout()

plt.show()


IB = (5 - VB) / (470 * 10**3) * 10**6  # μA
beta = (IC / 1000) / (IB / 10**6)


print("\nVALORES DE IB")
print("-" * 35)
print(f"{'VB (V)':>7} | {'IB (μA)':>10}")
print("-" * 35)

for i in range(len(IB)):
    print(f"{VB[i]:>7.2f} | {IB[i]:>10.2f}")

print("\nVALORES DE BETA")
print("-" * 60)
print(f"{'IC (mA)':>8} | {'IB (μA)':>10} | {'Beta':>8}")
print("-" * 60)

for i in range(len(beta)):
    print(f"{IC[i]:>8.2f} | " f"{IB[i]:>10.2f} | " f"{beta[i]:>8.1f}")
