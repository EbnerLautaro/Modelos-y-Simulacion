import numpy as np
import random
import math
from scipy.stats import chi2
from tabulate import tabulate


def estimate_t(N_list, N, P_list):
    assert sum(N_list) == N
    T = 0
    for Ni, Pi in zip(N_list, P_list, strict=True):
        T += pow(Ni - (N*Pi), 2) / (N*Pi)
    return T


def p_x():
    F = [0.0, 0.31, 0.53, 0.65, 0.75, 0.83, 0.89, 0.93, 0.97, 0.99, 1]
    U = random.random()
    i = 0
    while U > F[i]:
        i += 1
    assert i != 0
    return i


def simulacion_p_valor(t, gen, probs, n_sim):

    p_valor = 0
    for _ in range(n_sim):

        # calcular N_i
        muestra = []

        ocurrencias = [0 for _ in range(10)]
        for _ in range(637):
            elem = gen() - 1
            muestra.append(elem)
            ocurrencias[elem] += 1

        # calcular estimador T
        T = 0
        N = sum(ocurrencias)

        for i in range(len(ocurrencias)):
            T += pow(ocurrencias[i] - (N*probs[i]), 2)/(N*probs[i])

        if T >= t:
            p_valor += 1

    return p_valor / n_sim


if __name__ == "__main__":

    porcentajes = [x/100 for x in [31, 22, 12, 10, 8, 6, 4, 4, 2, 1]]
    ocurrencias = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
    table = {
        "Premio": list(range(1, 11)),
        "Areas (%)": porcentajes,
        "Ocurrencias": ocurrencias
    }
    print("tablita\n", tabulate(table, headers="keys"))

    N_list = ocurrencias
    P_list = porcentajes
    N = sum(N_list)
    t = estimate_t(N_list, N, P_list)
    df = 10-1
    print(f"Estimador t         {t}")
    print(f"p-valor Pearson     {chi2.sf(x=t, df=df)}")

    p_valor = simulacion_p_valor(
        t=t,
        gen=p_x,
        probs=porcentajes,
        n_sim=1_000,
    )
    print(f"simulacion p-valor  {p_valor}")
