import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

VS = 12.0  # V
VT = 25.85 * 10**-3  # V


def ajuste_linear(VD, a, b):
    lnID = a * VD + b
    return lnID


VR = np.array([9.46, 10.13, 10.43, 11.12, 11.16, 11.29, 11.43, 11.47])  # V
VD = VS - VR  # V
ID = np.array([43.00, 21.55, 10.43, 5.05, 2.37, 1.12, 0.24, 0.11])  # mA
lnID = np.log(ID * 10**-3)


poptab, _ = curve_fit(ajuste_linear, VD, lnID)

a = poptab[0]
b = poptab[1]

print("a: %.4f" % (a))
print("b: %.4f" % (b))

IS = np.exp(b)  # A
eta = 1 / (a * VT)

x = np.linspace(VD.min(), VD.max(), 300)  # V
y = (IS * np.exp(x / (eta * VT))) * 10**3  # mA


plt.figure(figsize=(9, 6))
plt.scatter(VD, ID, label="Exp")
plt.plot(x, y, "--", label="Ajuste")
plt.xlabel("$V_D$ (V)")
plt.ylabel("$I_D$ (mA)")

plt.grid(True, which="both", linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()

plt.show()
