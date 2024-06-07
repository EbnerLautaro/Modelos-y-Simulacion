import random, math
from scipy.stats import chi2
import numpy as np


def simulacion_p_valor(N, n_sim):
    n = 0
    cont = 0
    while n <= n_sim:
        N1 = np.random.binomial(n=N, p=(1 / 4))
        N2 = np.random.binomial(n=N - N1, p=(1 / 2) / (1 - (1 / 4)))
        N3 = np.random.binomial(n=N - N1 - N2, p=(1 / 4) / (1 - (1 / 4) - (1 / 2)))

        T = (N1 - N * (1 / 4)) ** 2 / (N * (1 / 4))
        T += (N2 - N * (1 / 2)) ** 2 / (N * (1 / 2))
        T += (N3 - N * (1 / 4)) ** 2 / (N * (1 / 4))

        if T > 0.8616:
            cont += 1

        n += 1

    return cont / n_sim


if __name__ == "__main__":

    print(f"p valor segun prueba de Pearson     {chi2.sf(x=0.8616, df=2)}")
    x = 0
    print(f"p valor simulacion                  {simulacion_p_valor(564, 10_000)}")
