import random
import math
from scipy import stats
import numpy as np


# def acumulada_poisson(x, mu):
#     return stats.poisson.cdf(x, mu)


def media_muestral(muestra):
    return sum(muestra) / len(muestra)


def estadistico_T(N_list, N, P_list):
    assert len(N_list) == len(P_list)
    assert sum(N_list) == N
    T = 0
    for Ni, Pi in zip(N_list, P_list):
        T += pow(Ni - (N*Pi), 2) / (N*Pi)
    return T


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
        t = estadistico_T(N=sum(N_list), N_list=N_list, P_list=probs)
        if t > T:
            cont += 1
        n += 1

    return cont/n_sim


if __name__ == "__main__":

    muestra = [0, 2, 5, 2, 2, 6, 3, 1, 2, 2, 4, 5, 4, 5, 1, 3, 3, 6, 4, 1]
    N = 7
    mu = 3
    ocurrencias = [0] * N
    for elem in muestra:
        if elem >= 6:
            ocurrencias[6] += 1
        else:
            ocurrencias[elem] += 1

    print(ocurrencias)

    assert sum(ocurrencias) == len(muestra)

    est_t = estadistico_T(
        N_list=ocurrencias,
        N=sum(ocurrencias),
        P_list=[stats.poisson.pmf(i, mu) for i in range(N)]
    )
    print(f"estimador T             {est_t}")

    p_valor = stats.chi2.sf(x=est_t, df=N-1)
    print(f"p-valor chi2            {p_valor}")

    p_valor = simulacion_p_valor_gen(
        N=sum(ocurrencias),
        probs=[stats.poisson.pmf(i, mu) for i in range(N)],
        T=est_t,
        n_sim=10_000
    )
    print(f"p-valor simulacion      {p_valor}")
