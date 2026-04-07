import numpy as np

from solenoide import calcular_B


def gerar_tabela_axial(indices, label):
    print("\n--- %s (mT) ---" % (label))

    idx = np.array(indices)
    N_sub = solenoides_N[idx]  # adimensional
    L_sub = solenoides_L[idx]  # mm
    d_sub = solenoides_d[idx]  # mm

    z = np.arange(0, 18, 1).reshape(-1, 1)  # cm

    B_matriz = calcular_B(N_sub, L_sub, d_sub, z)  # mT

    header = "z(cm) | " + " | ".join(
        [("Sol %i" % (i + 1)).center(7) for i in indices]
    )
    print(header)
    print("-" * len(header))

    for i in range(np.size(z)):
        linha = "%5i | " % (i)
        valores = ["%7.5f" % val for val in B_matriz[i]]
        print(linha + " | ".join(valores))


solenoides_N = np.array([75, 150, 300, 100, 200, 300, 300])  # adimensional
solenoides_L = np.array([160, 160, 160, 53, 105, 160, 160])  # mm
solenoides_d = np.array([25, 25, 25, 40, 40, 40, 32])  # mm

print(
    "--- TABELA 4.2: Densidade de fluxo magnético no centro dos solenoides ---"
)

B_zeros = calcular_B(solenoides_N, solenoides_L, solenoides_d, 0)  # mT

for i in range(np.size(solenoides_N)):
    print(
        "N = %3i, L = %3i mm, d = %2i mm -> B(0) = %.5f mT"
        % (solenoides_N[i], solenoides_L[i], solenoides_d[i], B_zeros[i])
    )


gerar_tabela_axial(
    [0, 1, 2], "TABELA 4.3: raio e comprimento fixos do solenoide"
)
gerar_tabela_axial([3, 4, 5], "TABELA 4.4: raio fixo")
gerar_tabela_axial([2, 5, 6], "TABELA 4.5: número de espiras fixo")
