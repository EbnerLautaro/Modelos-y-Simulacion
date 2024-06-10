import random
import math
from scipy.stats import chi2
import numpy as np


def estimador_T(N_list: list[int], N: int, p_list: list[float]):

    assert len(N_list) == len(p_list)
    assert sum(N_list) == N

    T = 0
    for ni, pi in zip(N_list, p_list):
        T += pow((ni - (N*pi)), 2)/(N*pi)
    return T


def simulacion_p_valor(N, n_sim):
    n = 0
    cont = 0
    while n <= n_sim:
        N1 = np.random.binomial(n=N, p=(1 / 4))
        N2 = np.random.binomial(n=N - N1, p=(1 / 2) / (1 - (1 / 4)))
        N3 = np.random.binomial(
            n=N - N1 - N2, p=(1 / 4) / (1 - (1 / 4) - (1 / 2)))

        T = (N1 - N * (1 / 4)) ** 2 / (N * (1 / 4))
        T += (N2 - N * (1 / 2)) ** 2 / (N * (1 / 2))
        T += (N3 - N * (1 / 4)) ** 2 / (N * (1 / 4))

        if T >= 0.8616:
            cont += 1

        n += 1

    return cont / n_sim


def simulacion_p_valor_gen(N, probs, T, n_sim):
    n = 0
    cont = 0
    while n <= n_sim:

        # calcular N_i
        N_list = []
        sum_probs = 0
        for prob in probs:
            N_i = np.random.binomial(
                n=N - sum(N_list),
                p=prob / (1-sum_probs),
            )
            N_list.append(N_i)
            sum_probs += prob

        # Calcular T
        t = 0
        for i in range(len(probs)):
            value = pow(N_list[i]-(N*probs[i]), 2) / (N*probs[i])
            t += value

        if t > T:
            cont += 1
        n += 1

    return cont/n_sim


if __name__ == "__main__":

    print(estimador_T([141, 291, 132], 564, [.25, .5, .25]))

    print(f"p valor de Pearson      {chi2.sf(x=0.8616, df=2)}")

    print(f"p valor simulacion      {simulacion_p_valor(564, 100_000)}")

    p_valor = simulacion_p_valor_gen(
        N=564, probs=[.25, .5, .25], T=0.8616, n_sim=100_000,
    )

    print(
        f"p valor simulacion2       {p_valor}")
