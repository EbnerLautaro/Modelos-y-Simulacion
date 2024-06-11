import random
import math
import numpy as np
from scipy import stats
from tabulate import tabulate


def simular_p_valor(d, N_sample, n_sim):

    def F_uniforme(x): return x

    p_valor = 0
    for _ in range(n_sim):

        N_list = np.random.uniform(0, 1, size=N_sample)
        N_list.sort()

        d_j = estadistico_d(N_list, F_uniforme)

        if d_j > d:
            p_valor += 1

    return p_valor/n_sim


def estadistico_d(muestra, F):
    m = muestra
    muestra.sort()
    d = 0
    n = len(m)
    for i in range(1, n+1):
        elem = m[i-1]
        d = max(d, (i/n)-F(elem), F(elem)-((i-1)/n))
    return d


def t_student(df):  # df grados de libertad
    x = random.gauss(0.0, 1.0)
    y = 2.0*random.gammavariate(0.5*df, 2.0)
    return x / (math.sqrt(y/df))


def acumulada_normal(x):
    return math.erf(x/math.sqrt(2.))/2.+0.5


if __name__ == "__main__":

    # P(X2 >= x) => chi2.sf(x, df)
    # P(X2 <= x) => chi2.cdf(x, df)

    estadisticos_d = []
    p_values = []
    N_samples = [10, 20, 100, 1000]
    for N_sample in N_samples:
        muestra = [t_student(11) for _ in range(N_sample)]
        d_stat = estadistico_d(muestra, acumulada_normal)
        p_valor = simular_p_valor(d=d_stat, N_sample=N_sample, n_sim=1_000)
        estadisticos_d.append(d_stat)
        p_values.append(p_valor)

    table = {
        "tamaño muestra": N_samples,
        "estadistico d": estadisticos_d,
        "p-valor": p_values
    }

    print(tabulate(table, headers="keys"))
