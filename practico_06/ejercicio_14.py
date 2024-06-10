import random
import math
import numpy as np
from scipy import stats


def estadistico_d(muestra, F):
    m = muestra
    muestra.sort()
    d = 0
    n = len(m)
    for i in range(1, n+1):
        elem = m[i-1]
        d = max(d, (i/n)-F(elem), F(elem)-((i-1)/n))
    return d


def acumulada_normal(x):
    return stats.norm.cdf(x)


if __name__ == "__main__":

    for N_sample in [10, 20, 100, 1000]:

        muestra = np.random.standard_t(11, size=N_sample)
        d_stat = estadistico_d(muestra, acumulada_normal)
        print(d_stat)
