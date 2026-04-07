import numpy as np


def calcular_erro_relativo(B_teorico, B_medido):
    teorico = np.array(B_teorico)
    medido = np.array(B_medido)

    erro_relativo = np.round(
        np.abs((teorico - medido) / teorico) * 100, 4
    )  # %
    return erro_relativo  # %


def gerar_tabela_axial(teoricos, medidos, label):
    print("\n--- %s (Erro Relativo) ---" % (label))

    z = np.arange(0, 18, 1)  # cm
    num_solenoides = len(teoricos)

    errorel_matriz = calcular_erro_relativo(teoricos, medidos).T  # %

    header = "z(cm) | " + " | ".join(
        [("Sol %i" % (i + 1)).center(7) for i in range(num_solenoides)]
    )
    print(header)
    print("-" * len(header))

    for i in range(np.size(z)):
        linha = "%5i | " % (i)
        valores = ["%6.2f%%" % val for val in errorel_matriz[i]]
        print(linha + " | ".join(valores))


tab1_teorico = [0.582, 1.164, 2.328, 1.893, 2.237, 2.286, 2.310]  # mT
tab1_medido = [0.54, 1.20, 2.33, 1.83, 2.17, 2.27, 2.27]  # mT

print(
    "--- TABELA 1: Densidade de fluxo magnético no centro dos solenoides (Erro Relativo) ---"
)

erro_tab1 = calcular_erro_relativo(tab1_teorico, tab1_medido)

for i in range(np.size(erro_tab1)):
    print("Configuração %i: Erro Relativo = %.2f%%" % (i + 1, erro_tab1[i]))


tab2_sol1_teorico = [
    0.582,
    0.582,
    0.581,
    0.578,
    0.574,
    0.565,
    0.543,
    0.477,
    0.294,
    0.110,
    0.044,
    0.022,
    0.013,
    0.008,
    0.006,
    0.004,
    0.003,
    0.002,
]  # mT, onde N = 75, L = 160 mm, d = 25 mm
tab2_sol1_medido = [
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
]  # mT, onde N = 75, L = 160 mm, d = 25 mm

tab2_sol2_teorico = [
    1.164,
    1.163,
    1.161,
    1.157,
    1.148,
    1.130,
    1.086,
    0.955,
    0.587,
    0.219,
    0.088,
    0.044,
    0.026,
    0.017,
    0.011,
    0.008,
    0.006,
    0.005,
]  # mT, onde N = 150, L = 160 mm, d = 25 mm
tab2_sol2_medido = [
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
]  # mT, onde N = 150, L = 160 mm, d = 25 mm

tab2_sol3_teorico = [
    2.328,
    2.327,
    2.322,
    2.313,
    2.296,
    2.260,
    2.172,
    1.910,
    1.175,
    0.439,
    0.176,
    0.088,
    0.051,
    0.033,
    0.023,
    0.017,
    0.013,
    0.010,
]  # mT, onde N = 300, L = 160 mm, d = 25 mm
tab2_sol3_medido = [
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


gerar_tabela_axial(
    [tab2_sol1_teorico, tab2_sol2_teorico, tab2_sol3_teorico],
    [tab2_sol1_medido, tab2_sol2_medido, tab2_sol3_medido],
    "TABELA 2: raio e comprimento fixos do solenoide",
)


tab3_sol1_teorico = [
    1.893,
    1.794,
    1.455,
    0.913,
    0.472,
    0.244,
    0.137,
    0.084,
    0.055,
    0.038,
    0.027,
    0.020,
    0.015,
    0.012,
    0.010,
    0.008,
    0.006,
    0.005,
]  # mT, onde N = 100, L = 53 mm, d = 40 mm
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

tab3_sol2_teorico = [
    2.237,
    2.223,
    2.173,
    2.058,
    1.804,
    1.323,
    0.758,
    0.393,
    0.216,
    0.129,
    0.084,
    0.057,
    0.041,
    0.031,
    0.024,
    0.019,
    0.015,
    0.012,
]  # mT, onde N = 200, L = 105 mm, d = 40 mm
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

tab3_sol3_teorico = [
    2.286,
    2.283,
    2.273,
    2.253,
    2.216,
    2.145,
    1.999,
    1.695,
    1.169,
    0.643,
    0.338,
    0.191,
    0.119,
    0.079,
    0.056,
    0.041,
    0.031,
    0.024,
]  # mT, onde N = 300, L = 160 mm, d = 40 mm
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

gerar_tabela_axial(
    [tab3_sol1_teorico, tab3_sol2_teorico, tab3_sol3_teorico],
    [tab3_sol1_medido, tab3_sol2_medido, tab3_sol3_medido],
    "TABELA 3: raio fixo",
)


tab4_sol1_teorico = [
    2.328,
    2.327,
    2.322,
    2.313,
    2.296,
    2.260,
    2.172,
    1.910,
    1.175,
    0.439,
    0.176,
    0.088,
    0.051,
    0.033,
    0.023,
    0.017,
    0.013,
    0.010,
]  # mT, onde N = 300, L = 160 mm, d = 25 mm
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

tab4_sol2_teorico = [
    2.286,
    2.283,
    2.273,
    2.253,
    2.216,
    2.145,
    1.999,
    1.695,
    1.169,
    0.643,
    0.338,
    0.191,
    0.119,
    0.079,
    0.056,
    0.041,
    0.031,
    0.024,
]  # mT, onde N = 300, L = 160 mm, d = 40 mm
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

tab4_sol3_teorico = [
    2.310,
    2.308,
    2.302,
    2.288,
    2.262,
    2.209,
    2.090,
    1.796,
    1.172,
    0.549,
    0.254,
    0.134,
    0.081,
    0.053,
    0.037,
    0.027,
    0.020,
    0.016,
]  # mT, onde N = 300, L = 160 mm, d = 32 mm
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

gerar_tabela_axial(
    [tab4_sol1_teorico, tab4_sol2_teorico, tab4_sol3_teorico],
    [tab4_sol1_medido, tab4_sol2_medido, tab4_sol3_medido],
    "TABELA 4: número de espiras fixo",
)
